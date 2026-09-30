# Open Challenge Strategy

## 1. Challenge Overview

Our current competition focus is the WRO Future Engineers 2026 Open Challenge.

The Open Challenge requires the vehicle to complete three laps on the track autonomously.

Unlike the Obstacle Challenge, the Open Challenge does not use traffic signs.

The internal wall configuration can change between challenge rounds, so the vehicle must be able to respond to the actual track configuration.

## 2. Track Variation

The WRO 2026 rules state that the distance between the track borders in the Open Challenge can vary between rounds.

The starting section and starting zone are also determined before each round.

Because the track configuration can change, a control strategy based only on a fixed sequence of timed turns would not be sufficient for a changing track.

Our vehicle therefore uses sensor information to support autonomous navigation.

## 3. Autonomous Operation

The vehicle must operate autonomously during the challenge.

The intended control process is:

1. Initialize the vehicle hardware.
2. Wait for the competition start.
3. Read sensor information.
4. Process the available sensor information.
5. Estimate the current track situation.
6. Calculate the steering command.
7. Control the propulsion system.
8. Continue navigating through the track.
9. Detect completion of the required laps.
10. Stop autonomously.

The exact implementation of these steps will be documented after the final competition software is completed.

## 4. Vision

The Pixy2 camera is part of our sensing system.

The camera provides visual information that can be processed by the software to support autonomous driving.

The final software documentation will explain:

- What information is extracted from the camera
- How the information is processed
- How the result affects steering
- How invalid or missing camera data is handled

## 5. Steering Control

The vehicle uses a parallel steering mechanism.

The software will generate a steering command based on the information available from the sensors.

The steering actuator then changes the direction of the steering wheels through the mechanical linkage.

The final software section will document the actual steering algorithm used by the competition program.

## 6. Drive Control

The propulsion system uses the mechanically coupled drive system described in the Motor Drive documentation.

The software controls the propulsion motors while respecting the mechanical drivetrain.

The vehicle is not controlled as an electronic left/right differential-drive system.

## 7. Corner Handling

The final control system must be able to handle straight sections and corners of the changing track.

The final implementation will document how the software identifies a change in the track and how it changes steering and speed.

Only the behavior implemented in the final competition software will be described here.

## 8. Lap Completion

The Open Challenge requires three complete laps.

The final software will include a method for identifying the vehicle's progress through the track and determining when the required number of laps has been completed.

The exact implementation will be documented after the final program is completed.

## 9. Finish

After completing three laps, the vehicle must autonomously finish the attempt according to the competition rules.

The final documentation will explain how our software recognizes the finish condition and commands the vehicle to stop.

## 10. Development Status

The Open Challenge software is currently under development.

The strategy described in this document represents the intended architecture rather than a claim that every part has already been successfully tested.

Physical test results will be added to the Tests section after they are performed.

## 11. Rules Reference

The WRO Future Engineers 2026 rules describe the Open Challenge as a three-lap autonomous race with changing internal wall placement and no traffic signs.

The vehicle must operate autonomously and must follow the challenge driving direction.

The final implementation will be checked against the competition rules before the competition.
