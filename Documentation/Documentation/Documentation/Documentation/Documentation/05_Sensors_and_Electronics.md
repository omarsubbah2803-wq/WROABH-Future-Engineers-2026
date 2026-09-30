# Sensors and Electronics

## 1. Controller

The vehicle uses a LEGO Mindstorms EV3 controller running EV3dev/Linux.

The controller is responsible for reading the sensors and controlling the vehicle's motors and steering system.

The control software is written in Python.

## 2. Pixy2 Camera

The Pixy2 is used as a vision sensor.

The camera provides visual information that can be processed by the robot's software to support autonomous driving.

The Pixy2 communicates with the EV3 using I2C.

The communication address used during development is:

0x54

The Pixy2 was successfully detected during communication testing, and the EV3 was able to read data from the camera.

The final software documentation will explain exactly how the vision data is processed and converted into steering decisions.

## 3. Ultrasonic Sensor

The ultrasonic sensor is used to measure distance.

In the current hardware configuration, the ultrasonic sensor is connected to EV3 input port 4.

The sensor can provide distance information to the autonomous control system.

Its exact role in the final Open Challenge program will be documented after the final software configuration is completed.

## 4. Color Sensors

Color sensors are available in the vehicle's hardware configuration.

The current development configuration used:

- Left color sensor: EV3 input port 2
- Right color sensor: EV3 input port 3

Their final role in the competition software will depend on the final implementation.

## 5. Motor Connections

The two known propulsion motors are connected to:

- Motor 1: EV3 output B
- Motor 2: EV3 output C

The final steering actuator connection will be verified and documented separately.

## 6. Wiring Architecture

The electrical system connects the EV3 controller to the propulsion motors, steering actuator and sensors.

The final repository should include a wiring diagram showing:

- EV3 controller
- Drive motors
- Steering actuator
- Pixy2
- Ultrasonic sensor
- Other sensors used in the final configuration

The wiring diagram should represent the actual physical vehicle rather than a theoretical configuration.

## 7. Sensor Placement

Sensor placement is important because each sensor needs a clear view or measurement path while remaining securely mounted to the vehicle.

The Pixy2 is positioned to observe the track.

The ultrasonic sensor is positioned to measure distance in the direction intended by the final control strategy.

The final documentation will include photographs showing the physical placement of these sensors.

## 8. Power

The EV3 provides the main control and power interface for the connected LEGO electronics.

The final documentation will record the actual battery configuration used during the competition.

Power measurements should only be added after they have been physically measured.

## 9. Communication

The Pixy2 communication was tested using the EV3 I2C interface during development.

A successful communication test returned sensor data from the Pixy2.

The final software will use the verified communication method rather than relying on an unverified external interface.

## 10. Error Handling

The final software should account for possible hardware problems such as:

- Sensor communication failure
- Missing Pixy2 data
- Invalid sensor readings
- Motor errors
- Sensor disconnection

The exact error-handling behavior will be documented after the final competition software is implemented.

## 11. Final Configuration

The final port map and wiring diagram will be updated before competition submission so that they match the physical robot exactly.
