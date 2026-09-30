# Sensors and Electronics

## 1. Controller

The vehicle uses a LEGO Mindstorms EV3 controller running EV3dev/Linux.

The controller is responsible for reading sensor information and controlling the vehicle's motors and steering system.

The control software is written in Python.

## 2. Pixy2 Camera

The Pixy2 is used as a vision sensor.

The camera provides visual information that can be processed by the robot's software to support autonomous driving.

During development, the Pixy2 communicates with the EV3 through the I2C interface.

The Pixy2 communication address used during development is:

0x54

The final software documentation will explain exactly how the vision data is processed and converted into steering decisions.

## 3. Ultrasonic Sensor

The ultrasonic sensor is used to measure distance.

In the current development configuration, the ultrasonic sensor is connected to EV3 input port 4.

The sensor provides distance information that can be used by the autonomous control system.

Its exact role in the final Open Challenge software will be documented after the final software configuration is completed.

## 4. Color Sensors

Color sensors are available in the vehicle's hardware configuration.

The current development configuration uses:

- Left color sensor: EV3 input port 2
- Right color sensor: EV3 input port 3

Their final role in the competition software depends on the final implementation.

## 5. Motor Connections

The two propulsion motors are connected to:

- Motor 1: EV3 output B
- Motor 2: EV3 output C

The final steering actuator connection will be verified and documented separately.

## 6. Wiring Architecture

The electrical system connects the EV3 controller to the propulsion motors, steering actuator and sensors.

The final repository should contain a wiring diagram showing:

- EV3 controller
- Drive motors
- Steering actuator
- Pixy2
- Ultrasonic sensor
- Other sensors used in the final configuration

The wiring diagram should represent the actual physical vehicle.

## 7. Sensor Placement

Sensor placement is important because each sensor needs a useful measurement or viewing area while remaining securely attached to the vehicle.

The Pixy2 is positioned to observe the track.

The ultrasonic sensor is positioned to measure distance in the direction intended by the control strategy.

The final documentation will include photographs showing the physical placement of these sensors.

## 8. Power

The vehicle uses the EV3 electrical system to power and control the connected electronics.

The final documentation will record the actual battery configuration used during the competition.

Power measurements and current consumption should only be added when they have been physically measured.

## 9. Communication

The Pixy2 communicates with the EV3 through I2C.

The final software will use the verified communication method and document the interface used by the competition program.

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
