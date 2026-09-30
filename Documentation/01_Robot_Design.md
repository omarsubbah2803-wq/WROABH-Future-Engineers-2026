# Robot Design

## Overview

Our vehicle is a four-wheeled autonomous vehicle designed for the WRO Future Engineers 2026 competition.

The main design objective is to combine a stable mechanical structure, a mechanically coupled drive system, a dedicated steering mechanism and autonomous sensing.

## Main Components

- LEGO Mindstorms EV3 controller
- LEGO Large Motors
- Four wheels
- Parallel steering mechanism
- Pixy2 camera
- Ultrasonic sensor
- LEGO Technic structural components
- Mechanical gears and linkages

## Chassis

The chassis supports the EV3 controller, drive system, steering mechanism, sensors and wheels.

The structure is designed to remain rigid so that movement of the chassis does not unnecessarily affect wheel alignment, steering or sensor position.

The compact structure also allows the main components to remain securely attached while leaving enough space for the steering and drivetrain mechanisms.

## Steering

The current vehicle uses a parallel steering mechanism.

The steering wheels are mechanically connected through a linkage and are controlled by a steering actuator.

The steering mechanism changes the direction of the vehicle while the drivetrain remains responsible for propulsion.

## Drive System

The propulsion system transfers motor rotation through a mechanical drivetrain to the driving axle and wheels.

The drivetrain is mechanically coupled rather than being controlled as an electronic left/right differential system.

This separation allows the vehicle to use a dedicated steering mechanism instead of changing direction by independently controlling the left and right sides.

## Sensors

The vehicle uses a Pixy2 camera as part of its vision system and an ultrasonic sensor for distance measurement.

The sensor positions are selected so that they can provide useful information for autonomous navigation while remaining securely mounted to the vehicle.

The final software documentation will describe how the sensor information is processed.

## Design Constraints

The WRO Future Engineers 2026 rules require a four-wheeled vehicle with one driving axle and one steering actuator.

The rules also prohibit a differential-wheeled base and the use of an electronic differential with one motor per side.

The vehicle must also remain within the maximum dimensions and weight specified by the competition rules.

## Design Approach

Our design separates the vehicle into several main systems:

- Mechanical frame
- Steering system
- Drive system
- Sensors
- Controller
- Software

Each subsystem has a specific function, but all of them must work together for autonomous driving.

## Current Status

The mechanical vehicle has been assembled.

The current steering concept is parallel steering.

The final competition software is still under development, so final performance measurements and physical test results will be added after testing.
