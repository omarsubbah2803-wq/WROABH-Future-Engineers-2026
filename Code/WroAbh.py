#!/usr/bin/env python3
"""
Ultrasonic Gap-Detection Navigation (WRO Future Engineers)
Reads the starting color to determine direction, then uses the inner wall's gaps 
to trigger 90-degree turns for 4 laps (16 corners) with Gyro stabilization.
Python 3.5 Compatible. Normal Speed Edition.
"""
import time
import math
import colorsys

# ---------------- HARDWARE SETTINGS ----------------
DRIVE_PORT = 'outB'
STEER_PORT = 'outA'
LEFT_PORT = 'in4'
RIGHT_PORT = 'in1'
COLOR_PORT = 'in3'
GYRO_PORT = 'in2'

GYRO_SIGN = 1
DRIVE_SIGN = 1
STEER_SIGN = 1

WHEEL_DIAMETER_MM = 56.0
MOTOR_ROTATIONS_PER_WHEEL = 1.0
STEER_LIMIT_DEG = 75
TURN_MOTOR_DEG = 60

# --- NORMAL SPEED SETTINGS ---
STRAIGHT_DPS = 500            # Stable straight speed
TURN_DPS = 300                # Controlled cornering speed
STEER_DPS = 500               # Smooth steering adjustments
# ---------------------------

# Geometry & Gap Detection Thresholds
GAP_THRESHOLD_CM = 40.0       
TURN_CLEARANCE_MM = 150.0     # Safely clears the physical corner block before turning
TARGET_WALL_DIST_CM = 15.0    
FINISH_ADVANCE_MM = 600.0     

# PID Control for straight driving
WALL_KP = 2.5
WALL_KD = 0.5
GYRO_HEADING_KP = 2.0
# ----------------------------------------------------

WHITE_RGB = (300.0, 300.0, 300.0)
MIN_BRIGHTNESS = 0.06
MIN_SATURATION = 0.40
ORANGE_HUE = (5.0, 55.0)
BLUE_HUE = (185.0, 265.0)


def clamp(x, low, high):
    return max(low, min(high, x))


def classify(raw):
    rgb = [min(1.0, max(0.0, float(v) / w)) for v, w in zip(raw, WHITE_RGB)]
    h, s, v = colorsys.rgb_to_hsv(*rgb)
    h *= 360.0
    
    if v < MIN_BRIGHTNESS or s < MIN_SATURATION:
        return None
    if ORANGE_HUE[0] <= h <= ORANGE_HUE[1]:
        return 1  # 1 = Clockwise (Right)
    if BLUE_HUE[0] <= h <= BLUE_HUE[1]:
        return -1 # -1 = Counter-Clockwise (Left)
    return None


class Robot:
    def __init__(self):
        from ev3dev2.motor import Motor
        from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor, GyroSensor
        from ev3dev2.button import Button
        
        self.drive = Motor(DRIVE_PORT)
        self.steer = Motor(STEER_PORT)
        self.left = UltrasonicSensor(LEFT_PORT)
        self.right = UltrasonicSensor(RIGHT_PORT)
        self.color = ColorSensor(COLOR_PORT)
        self.gyro = GyroSensor(GYRO_PORT)
        
        self.left.mode = 'US-DIST-CM'
        self.right.mode = 'US-DIST-CM'
        self.color.mode = 'RGB-RAW'
        
        self.gyro_zero = 0.0
        self.buttons = Button()
        self.target = None
        self.speed = None

    def mm(self):
        return (DRIVE_SIGN * self.drive.position * math.pi * WHEEL_DIAMETER_MM
                / (360.0 * MOTOR_ROTATIONS_PER_WHEEL))

    def heading(self):
        return GYRO_SIGN * self.gyro.angle - self.gyro_zero

    def steering(self, logical_angle):
        target = int(STEER_SIGN * clamp(logical_angle, -STEER_LIMIT_DEG, STEER_LIMIT_DEG))
        if self.target != target:
            self.steer.run_to_abs_pos(position_sp=target, speed_sp=STEER_DPS, stop_action='hold')
            self.target = target

    def forward(self, dps):
        if self.speed != dps:
            self.drive.run_forever(speed_sp=int(DRIVE_SIGN * dps))
            self.speed = dps

    def stop_drive(self):
        self.drive.stop(stop_action='brake')
        self.speed = None

    def stop(self):
        self.stop_drive()
        self.steer.stop(stop_action='hold')

    def prepare(self):
        self.stop_drive()
        self.steer.stop(stop_action='coast')
        
        print('Wheels must be centered BEFORE launching this program.', flush=True)
        self.steer.position = 0
        self.drive.position = 0
        self.steering(0)
        
        print('Keep robot STILL. Calibrating gyro...', flush=True)
        self.gyro.mode = 'GYRO-RATE'
        time.sleep(1.0)
        self.gyro.mode = 'GYRO-ANG'
        time.sleep(1.0)
        
        print('Ready! Press and release CENTER button to start.', flush=True)
        while not self.buttons.enter:
            time.sleep(0.02)
        while self.buttons.enter:
            time.sleep(0.02)
            
        self.gyro_zero = GYRO_SIGN * self.gyro.angle


def run(robot):
    robot.prepare()
    direction = 0  
    state = 'detect_direction'
    
    completed_corners = 0
    turn_target_heading = 0
    advance_start_mm = 0
    gap_counter = 0  
    
    last_dist_error = None
    last_time = time.monotonic()
    
    print("Driving straight to detect color...", flush=True)
    
    while True:
        if robot.buttons.backspace:
            print("Aborted by user EV3 Back button.", flush=True)
            break

        pos = robot.mm()
        left_dist = robot.left.distance_centimeters
        right_dist = robot.right.distance_centimeters
        current_heading = robot.heading()
        current_time = time.monotonic()

        inner_dist = (right_dist if direction == 1 else left_dist) if direction != 0 else 0.0
        target_heading = direction * 90.0 * completed_corners

        if state == 'detect_direction':
            robot.forward(STRAIGHT_DPS)
            robot.steering((target_heading - current_heading) * GYRO_HEADING_KP)
            
            color_val = classify(robot.color.raw)
            if color_val is not None:
                direction = color_val
                print("Direction locked: {}".format('CW (Right)' if direction == 1 else 'CCW (Left)'), flush=True)
                state = 'follow_wall'
                last_dist_error = None
                
        elif state == 'follow_wall':
            robot.forward(STRAIGHT_DPS)
            
            if inner_dist > GAP_THRESHOLD_CM:
                gap_counter += 1
            else:
                gap_counter = 0
                
            if inner_dist < GAP_THRESHOLD_CM:
                dist_err = inner_dist - TARGET_WALL_DIST_CM
                dt = current_time - last_time
                if dt > 0.001 and last_dist_error is not None:
                    derivative = (dist_err - last_dist_error) / dt
                else:
                    derivative = 0.0
                    
                last_dist_error = dist_err
                last_time = current_time
                
                dist_correction = ((dist_err * WALL_KP) + (derivative * WALL_KD)) * direction
                heading_correction = (target_heading - current_heading) * GYRO_HEADING_KP
                robot.steering(dist_correction + heading_correction)
            else:
                robot.steering((target_heading - current_heading) * GYRO_HEADING_KP)
                last_dist_error = None
                
            if gap_counter >= 5:
                print("Space detected! Advancing into the corner...", flush=True)
                state = 'advance_into_space'
                advance_start_mm = pos
                gap_counter = 0
                last_dist_error = None
                
        elif state == 'advance_into_space':
            robot.forward(STRAIGHT_DPS)
            robot.steering((target_heading - current_heading) * GYRO_HEADING_KP)
            
            if pos - advance_start_mm >= TURN_CLEARANCE_MM:
                print("Turning into space.", flush=True)
                state = 'turn'
                turn_target_heading = direction * 90.0 * (completed_corners + 1)
                
        elif state == 'turn':
            robot.forward(TURN_DPS)
            robot.steering(direction * TURN_MOTOR_DEG)
            
            # Restored to 2.0 degrees for precise, non-skid turn completion
            corner_done = False
            if direction == 1 and current_heading >= turn_target_heading - 2.0:
                corner_done = True
            elif direction == -1 and current_heading <= turn_target_heading + 2.0:
                corner_done = True
            
            if corner_done: 
                completed_corners += 1
                robot.steering(0)
                print("Completed corner {}/16".format(completed_corners), flush=True)
                
                if completed_corners >= 16:
                    state = 'final_straight'
                    advance_start_mm = pos
                else:
                    state = 'recover'
                    
        elif state == 'recover':
            robot.forward(STRAIGHT_DPS)
            robot.steering((target_heading - current_heading) * GYRO_HEADING_KP)
            
            if inner_dist < GAP_THRESHOLD_CM:
                state = 'follow_wall'
                last_time = current_time
                
        elif state == 'final_straight':
            robot.forward(STRAIGHT_DPS)
            robot.steering((target_heading - current_heading) * GYRO_HEADING_KP)
            
            if pos - advance_start_mm >= FINISH_ADVANCE_MM:
                robot.stop()
                print("4 Laps complete. Parked inside Start/Finish box.", flush=True)
                break
            
        time.sleep(0.02)


if __name__ == '__main__':
    r = Robot()
    try:
        run(r)
    except KeyboardInterrupt:
        r.stop()
    except Exception as e:
        print("Hardware Error/Stall: {}".format(e), flush=True)
        r.stop()
    finally:
        r.stop()
