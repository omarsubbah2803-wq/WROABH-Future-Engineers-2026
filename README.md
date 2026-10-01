WROABH Future Engineers 2026 – Autonomous Self-Driving Vehicle

1. Project Overview

This repository documents our WRO Future Engineers 2026 autonomous vehicle.

Our project focuses on designing, building and programming a four-wheeled autonomous vehicle that can navigate the WRO Future Engineers track without remote control.

The vehicle combines mechanical engineering, electronics, sensing, computer vision and autonomous control. The current design uses a mechanically coupled drive system and a dedicated parallel steering mechanism.

The vehicle is based on a LEGO Mindstorms EV3 controller running EV3dev/Linux. It uses two LEGO Medium Motors, a Pixy2 camera for the Obstacle Challenge, color sensors, a gyro sensor and ultrasonic sensors.

The purpose of this repository is to document our engineering process, design decisions, technical architecture and competition software.

2. Competition

The project is designed for the WRO Future Engineers 2026 self-driving car challenge.

Our current focus is the Open Challenge. The vehicle is designed to autonomously complete three laps while responding to the actual track configuration.

Because the track layout can change, the robot cannot rely only on a fixed sequence of timed movements. It needs to use sensor information and autonomous control to react to the track.

3. Vehicle Architecture

The vehicle is a four-wheeled autonomous car.

Main components:

- LEGO Mindstorms EV3 controller
- Two LEGO Medium Motors
- Mechanically coupled drive system
- Parallel steering mechanism
- Pixy2 camera
- Two color sensors
- Gyro sensor
- Ultrasonic sensors
- LEGO Technic structure
- Mechanical gears and linkages

The propulsion system and steering system are treated as separate mechanical subsystems.

4. Mechanical Design

The chassis is built using LEGO Technic structural components.

The structure supports the EV3 controller, motors, steering mechanism, sensors and wheels.

Mechanical rigidity is important because unwanted movement in the frame can affect steering accuracy, wheel alignment and sensor position.

The current design was developed with the goal of maintaining a compact, stable and understandable mechanical structure.

5. Parallel Steering

Our current vehicle uses parallel steering.

The two steering wheels are connected by a mechanical linkage so that they turn together at approximately the same steering angle.

This differs from Ackermann steering. In Ackermann steering, the inner wheel turns through a larger angle than the outer wheel during a corner.

We considered both steering concepts during development.

We selected parallel steering because it provides a simpler mechanical linkage with the LEGO Technic components available to our team. The steering motor transfers its movement through the linkage to both steering wheels.

Mechanical stiffness and low unwanted play are important because mechanical backlash can cause the actual steering position to differ from the intended steering command.

A technical comparison between parallel and Ackermann steering is included in the Documentation directory.

6. Motor Drive System

The propulsion system converts electrical energy into mechanical motion.

The LEGO Medium Drive Motor generates rotational motion. This rotation is transferred through the mechanical drivetrain and gears to the driving axle and wheels.

The steering system uses the second Medium Motor to actuate the parallel steering mechanism.

The gear train is important because the gear sizes determine the relationship between motor speed and axle speed.

A reduction gear can trade some output speed for increased torque. This can help the vehicle move the wheels with sufficient force while maintaining controllable motion.

The exact final gear ratio will be documented after it is verified from the physical drivetrain.

7. Previous Design and Design Change

During development, we considered an earlier vehicle concept with a different propulsion and steering arrangement.

The previous concept was not selected for the current competition vehicle.

For the current vehicle, we developed a mechanically coupled drive arrangement together with a dedicated steering mechanism.

This provides a clear mechanical separation between driving and steering and matches the architecture selected for the current vehicle.

The development history section of this repository records the evolution from the previous concept to the current design.

8. Sensors

Pixy2 Camera

The Pixy2 is used as a vision sensor during the Obstacle Challenge.

It provides visual information that can be processed by the autonomous software.

During the Obstacle Challenge configuration, the Pixy2 is connected to EV3 Input Port 1 and communicates through I2C.

Color Sensors

The vehicle uses two color sensors.

For the Open Challenge:

- Input 1 — Left Color Sensor
- Input 3 — Right Color Sensor

The color sensors provide track information for the autonomous control system.

Gyro Sensor

The gyro sensor is connected to Input Port 2.

It provides orientation and rotation information that can be used to support controlled turns and heading correction.

Ultrasonic Sensors

The Open Challenge configuration uses two ultrasonic sensors:

- Input 1 — Left Ultrasonic Sensor
- Input 2 — Right Ultrasonic Sensor

They provide distance information that can be used for wall detection and autonomous navigation.

«Note: The exact sensor configuration used by the final competition software must always match the physical robot.»

9. Motor Configuration

The current motor configuration is:

- Output A — Medium Drive Motor
- Output B — Medium Steering Motor

The drive motor provides propulsion through the mechanically coupled drivetrain.

The steering motor controls the parallel steering mechanism.

10. Software

The vehicle software runs on EV3dev/Linux using Python.

The software is designed to separate hardware access from control logic where practical.

The software includes or is intended to include:

- Hardware initialization
- Motor control
- Steering control
- Sensor reading
- Autonomous control logic
- Safety and error handling
- Configuration parameters

The final source code will be placed in the "Code" directory.

The final software documentation will be updated to match the actual implemented program.

11. Open Challenge Strategy

The Open Challenge requires the vehicle to respond to the actual track rather than depend only on a fixed sequence of timed movements.

The autonomous control system is intended to:

1. Initialize the hardware.
2. Wait for the competition start command.
3. Read sensor information.
4. Estimate the vehicle's current situation.
5. Calculate steering commands.
6. Control the drive system.
7. Detect progress through the track.
8. Continue until the required laps are complete.
9. Stop autonomously.

The exact implementation is documented and updated as the competition software is developed.

12. Development Process

Our engineering process follows an iterative approach:

Plan → Build → Test → Measure → Improve

When a mechanical or software change is made, we aim to record:

- What problem was observed
- What change was made
- Why the change was selected
- What result was observed
- What the next improvement should be

The purpose of this repository is therefore not only to show the final robot, but also to show how engineering decisions were made.

13. Testing

Testing is documented separately in the "Tests" directory.

Each physical test should record the actual robot version, configuration, objective, observed behavior and result.

We do not claim a successful result unless the corresponding test was actually performed.

As development continues, test records will be added to show how mechanical and software changes affect the vehicle.

14. Repository Structure

WROABH-Future-Engineers-2026/
│
├── README.md
├── Code/
├── CAD/
├── Electronics/
├── Documentation/
├── Media/
└── Tests/

Code

Contains the software used by the vehicle.

CAD

Contains mechanical design files and models where available.

Electronics

Contains wiring information, port maps and electrical documentation.

Documentation

Contains engineering explanations, development history and project information.

Media

Contains photographs of the real vehicle and technical reference images.

Tests

Contains real test records and measured results.

15. Reproducibility

A key purpose of the repository is reproducibility.

The documentation should give another team enough information to understand the major subsystems and how they interact.

For this reason, the final repository will include:

- Source code
- Mechanical design information
- Wiring information
- Robot photographs
- Software structure
- Engineering decisions
- Testing records
- Relevant CAD files

The goal is that another team can understand how the vehicle was constructed and how its software interacts with the physical hardware.

16. Final Vehicle Documentation

The final documentation will include photographs of the real vehicle.

The photographs will show the actual competition vehicle from multiple views and include detailed views of important mechanisms such as the steering system and drive system.

Only photographs of the real competition vehicle are used as vehicle documentation.

Technical reference images are stored separately and are clearly identified as references.

17. Project Status

Current status:

- Vehicle assembled
- Parallel steering selected
- Mechanically coupled drive system developed
- EV3 controller used as the main controller
- Two Medium Motors installed
- Pixy2 available for the Obstacle Challenge
- Two color sensors available for track sensing
- Gyro sensor installed
- Ultrasonic sensors available for distance measurement
- Competition software under development
- Physical testing and measured results to be added as completed

This repository will be updated as the project progresses.

18. Engineering Decisions

One important engineering decision was the choice of parallel steering.

We considered Ackermann steering as an alternative. Ackermann steering can provide different steering angles for the inner and outer wheels during a turn.

Our current design uses parallel steering because the linkage is simpler to implement with the available LEGO Technic components and provides a direct mechanical connection between the steering actuator and both steering wheels.

Another important decision was the change from the earlier propulsion concept to the current mechanically coupled drive arrangement.

The current design separates propulsion from steering rather than using the vehicle as a differential-drive system.

These decisions are documented in more detail in the "Documentation" directory.

19. WRO Documentation

The WRO Future Engineers documentation combines an Engineering Journal with a public GitHub repository.

The documentation is intended to show the engineering process, design decisions, systems thinking and reproducibility of the vehicle.

The repository therefore focuses on explaining not only what was built, but why the team selected the current architecture and how the system was developed.

All final statements about measurements, testing and performance will be based on the actual vehicle and the team's real work.

20. Team

Team Name: WROABH

Team Members:

- Omar Ahmad
- Omar Mahmmod

---

WRO Future Engineers 2026
