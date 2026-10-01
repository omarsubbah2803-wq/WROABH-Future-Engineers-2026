# Wiring Diagram

## System Overview

The LEGO Mindstorms EV3 controller is the central controller of the vehicle.

It communicates with the sensors and controls the vehicle's motors and steering actuator.

The main electrical connections are:

EV3 Controller
├── Drive Motor 1 → Output B
├── Drive Motor 2 → Output C
├── Steering Actuator → To be verified
├── Pixy2 Camera → I2C
├── Ultrasonic Sensor → Input 4
├── Left Color Sensor → Input 2
└── Right Color Sensor → Input 3

## Motor Connections

The propulsion motors are connected to EV3 outputs B and C.

These motors provide the mechanical power for the vehicle's drivetrain.

## Steering Connection

The steering actuator is connected to the EV3 controller through an output port.

The exact final port will be verified on the physical competition vehicle before submission.

## Pixy2 Connection

The Pixy2 camera communicates with the EV3 through the I2C interface.

The communication interface was verified during development.

## Ultrasonic Sensor

The ultrasonic sensor is connected to EV3 input port 4.

It provides distance measurements to the control software.

## Color Sensors

The current development configuration uses:

- Left color sensor → Input 2
- Right color sensor → Input 3

Their final role in the competition software will depend on the final implementation.

## Final Verification

The wiring diagram must match the actual competition vehicle.

Before the final submission, the team will verify:

- Every motor connection
- Steering actuator connection
- Every sensor connection
- Cable routing
- Physical sensor placement
- Final EV3 port assignments

Only verified connections should be treated as the final configuration.
