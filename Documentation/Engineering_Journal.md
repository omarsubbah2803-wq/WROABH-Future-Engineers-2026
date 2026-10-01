# Engineering Journal

## Project

WRO Future Engineers 2026

## Team

WROABH

## 1. Project Overview

Our project is a four-wheeled autonomous vehicle developed for the WRO Future Engineers 2026 competition.

The vehicle combines mechanical design, electronics, sensors and autonomous software.

## 2. Mechanical Design

The vehicle uses a LEGO Technic structure with a mechanically connected drive system and a dedicated parallel steering mechanism.

The chassis supports the EV3 controller, motors, sensors and steering system.

## 3. Steering System

Our current vehicle uses parallel steering.

The two steering wheels are connected through a mechanical linkage and are controlled by a steering actuator.

Ackermann steering was considered as an alternative, but parallel steering was selected because its linkage is simpler to implement with the available LEGO Technic components.

## 4. Drive System

The vehicle uses LEGO Large Motors for propulsion.

Motor rotation is transferred through a mechanical gear system to the driving axle and wheels.

The gear system creates a trade-off between speed and torque.

## 5. Sensors and Electronics

The vehicle uses:

- LEGO Mindstorms EV3
- Pixy2 camera
- Ultrasonic sensor
- Color sensors
- LEGO Large Motors

The Pixy2 is used as a vision sensor and communicates with the EV3 through I2C.

The ultrasonic sensor provides distance measurements.

## 6. Software

The final software runs on EV3dev/Linux using Python.

The software is designed to read sensor information and control propulsion and steering autonomously.

The final code will be added to the Code directory.

## 7. Open Challenge

Our current competition focus is the Open Challenge.

The Open Challenge requires the vehicle to autonomously complete three laps.

The internal wall configuration can change between rounds, so the vehicle needs to react to the current track rather than depend only on a fixed sequence of timed movements.

## 8. Engineering Decisions

Important decisions included:

- Selecting a mechanically connected drive system
- Selecting parallel steering
- Separating propulsion from steering
- Using Pixy2 for vision
- Using ultrasonic sensing for distance information

Each decision was considered in relation to the vehicle architecture, available components and competition requirements.

## 9. Development Process

Our development process follows:

Plan → Build → Test → Improve

Important changes are documented with their reason and actual result.

## 10. Testing

Physical test results will be added after the robot is tested.

Only real measurements and observations will be included.

## 11. Reproducibility

The GitHub repository is organized so that the mechanical design, electronics, software and documentation can be understood as connected parts of the same system.

Final code, CAD files, wiring diagrams and testing records will be added as they are completed.
