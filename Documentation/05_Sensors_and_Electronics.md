Sensors and Electronics

1. Controller

The vehicle uses a LEGO Mindstorms EV3 controller running EV3dev/Linux.

The controller is responsible for reading sensor information and controlling the drive and steering motors.

The control software is written in Python.

2. Pixy2 Camera

The Pixy2 is used as the main vision sensor for the Obstacle Challenge.

The camera provides visual information that can be processed by the robot's software to support autonomous driving and obstacle detection.

During the Obstacle Challenge configuration, the Pixy2 is connected to:

"EV3 Input Port 1"

The Pixy2 communicates with the EV3 through the I2C interface.

The Pixy2 communication address used during development is:

"0x54"

For the Open Challenge configuration, the Pixy2 is removed and the left color sensor is connected to Input Port 1 instead.

3. Color Sensors

The vehicle uses two color sensors.

The left color sensor is connected to:

"EV3 Input Port 1"

during the Open Challenge configuration.

The right color sensor is connected to:

"EV3 Input Port 3"

The left color sensor shares Input Port 1 with the Pixy2, depending on the competition configuration.

Obstacle Challenge

- Port 1: Pixy2 Camera
- Port 3: Right Color Sensor

Open Challenge

- Port 1: Left Color Sensor
- Port 3: Right Color Sensor

The color sensors provide information that can be used by the autonomous control system according to the selected challenge.

4. Gyro Sensor

The gyro sensor is connected to:

"EV3 Input Port 2"

The gyro sensor provides orientation and rotation information.

It can be used by the autonomous control system to monitor the vehicle's heading and support controlled turns.

5. Ultrasonic Sensor

The ultrasonic sensor is connected to:

"EV3 Input Port 4"

The sensor measures the distance between the vehicle and nearby objects or walls.

The distance information can be used by the autonomous control system for navigation and obstacle-related decisions.

6. Motor Connections

The vehicle uses two LEGO Medium Motors.

The current motor configuration is:

- Drive motor: EV3 Output A
- Steering motor: EV3 Output B

The drive motor provides propulsion through the mechanically coupled drivetrain.

The steering motor actuates the steering mechanism.

7. Port Configuration

The current configurations for the two challenges are:

Obstacle Challenge

EV3 Port| Component
Input 1| Pixy2 Camera
Input 2| Gyro Sensor
Input 3| Right Color Sensor
Input 4| Ultrasonic Sensor
Output A| Medium Drive Motor
Output B| Medium Steering Motor

Open Challenge

EV3 Port| Component
Input 1| Left Color Sensor
Input 2| Gyro Sensor
Input 3| Right Color Sensor
Input 4| Ultrasonic Sensor
Output A| Medium Drive Motor
Output B| Medium Steering Motor

The same EV3 controller and motor configuration are used for both challenge configurations.

The main change is the sensor connected to Input Port 1.

8. Wiring Architecture

The electrical system connects the EV3 controller to the drive motor, steering motor and sensors.

The wiring is organized according to the selected challenge configuration.

The final wiring documentation should represent the actual physical vehicle.

9. Sensor Placement

Sensor placement is important because each sensor needs a useful measurement or viewing area while remaining securely attached to the vehicle.

The Pixy2 is positioned to provide a clear view of the track during the Obstacle Challenge.

The left and right color sensors are positioned to provide useful track information during the Open Challenge.

The gyro sensor is mounted securely so that vehicle rotation can be measured consistently.

The ultrasonic sensor is positioned to measure distance in the direction required by the autonomous control strategy.

10. Communication

The Pixy2 communicates with the EV3 through the I2C interface.

The Pixy2 communication address used during development is:

"0x54"

The other sensors communicate directly with the EV3 through their respective input ports.

11. Power

The vehicle uses the EV3 electrical system to power and control the connected electronics.

The final documentation will record the actual battery configuration used during the competition.

Power measurements and current consumption will only be added when they have been physically measured.

12. Error Handling

The autonomous software should account for possible hardware problems such as:

- Sensor communication failure
- Missing Pixy2 data
- Invalid sensor readings
- Motor errors
- Sensor disconnection
- Unexpected sensor values

The exact error-handling behavior will be documented with the final competition software.

13. Final Configuration

The final port configuration is designed to match the physical vehicle.

The main difference between the two challenge configurations is the component connected to EV3 Input Port 1:

- Obstacle Challenge: Pixy2 Camera
- Open Challenge: Left Color Sensor

The remaining sensor and motor connections stay the same:

- Input 2: Gyro Sensor
- Input 3: Right Color Sensor
- Input 4: Ultrasonic Sensor
- Output A: Medium Drive Motor
- Output B: Medium Steering Motor

This configuration allows the same vehicle architecture to support both challenge configurations while changing the required sensor on Input Port 1.
