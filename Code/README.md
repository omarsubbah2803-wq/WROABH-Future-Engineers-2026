WRO Future Engineers - Ultrasonic Gap-Detection Navigation
This repository contains the Python 3.5 compatible ev3dev2 control software for the WRO Future Engineers open challenge. The robot uses a color sensor to determine the track direction, and a combination of ultrasonic sensors and a gyro sensor to navigate the track by detecting gaps in the central inner block.

Hardware Configuration
Ensure your EV3 motors and sensors are plugged into the correct ports. If your wiring differs, update the HARDWARE SETTINGS section at the top of the Python script.

Drive Motor: outB

Steering Motor: outA

Left Ultrasonic Sensor: in4

Right Ultrasonic Sensor: in1

Color Sensor: in3 (Mounted pointing down at the mat)

Gyro Sensor: in2 (Mounted securely, flat to the chassis)

How the Algorithm Works
Direction Detection: The robot drives straight off the start line while reading the color sensor.

Orange: Locks direction to Clockwise (Right).

Blue: Locks direction to Counter-Clockwise (Left).

Straightaways (PD + Gyro Control): The robot selects the ultrasonic sensor facing the inner wall (Left or Right, depending on direction). It uses a Proportional-Derivative (PD) controller to maintain exactly 15cm (TARGET_WALL_DIST_CM) from the inner wall. Simultaneously, the gyro locks the heading (0°, 90°, 180°, etc.) to prevent the robot from snaking or oscillating.

Gap Detection: When the ultrasonic sensor passes the physical corner of the central block, the distance reading spikes. If the reading stays above 40cm (GAP_THRESHOLD_CM) for 5 consecutive sensor frames, the robot confirms it has found a valid turning space.

Cornering: The robot drives forward 150mm (TURN_CLEARANCE_MM) to physically clear the corner block, then cuts the steering wheel to execute a gyro-monitored 90-degree turn.

Completion: After completing 16 corners (4 full laps), the robot drives straight for an additional 600mm (FINISH_ADVANCE_MM) to park cleanly inside the Start/Finish box.

How to Run
Place the robot in the Start/Finish box facing forward.

Manually center the front steering wheels. The code assumes the wheels are perfectly straight at launch.

Execute the script on the EV3 brick via SSH or the VS Code EV3dev extension.

Do not touch the robot. The program pauses for 2 seconds upon launch to calibrate the Gyro sensor. Moving the robot during this phase will cause fatal drifting.

When the EV3 console prints Ready!, press the CENTER (Enter) button on the EV3 brick to start the run.

Emergency Stop: Press the BACK button on the EV3 brick at any time to immediately abort the program and cut power to the motors.

Key Tuning Variables
If the robot's mechanical design (wheel size, steering linkage) differs from the reference model, adjust these constants in the script:

TURN_CLEARANCE_MM = 150.0: Increase this if the rear wheels clip the central wall during a turn. Decrease it if the robot turns too late and hits the outer wall.

FINISH_ADVANCE_MM = 600.0: Adjust this to change exactly where the robot parks after the final turn.

TARGET_WALL_DIST_CM = 15.0: The distance the robot attempts to keep from the inner block.

STRAIGHT_DPS = 500 / TURN_DPS = 300: Motor speeds in degrees-per-second. Max safe speed is typically around 850.

WALL_KP = 2.5 / WALL_KD = 0.5: The PD tuning values. Increase KP if it reacts too slowly to the wall; increase KD if it wiggles too aggressively.

WHITE_RGB = (300.0, 300.0, 300.0): Update this with the raw RGB values your color sensor reads when placed on the white part of the mat. This ensures accurate Orange/Blue classification in varying room lighting.
