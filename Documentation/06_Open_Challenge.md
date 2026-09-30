# Open Challenge Strategy

## 1. Challenge Overview

Our current competition focus is the WRO Future Engineers 2026 Open Challenge.

The Open Challenge requires the autonomous vehicle to complete three laps on the track.

Unlike the Obstacle Challenge, the Open Challenge does not use traffic signs.

The internal wall configuration can change between challenge rounds, so the vehicle must be able to respond to the actual track configuration.

## 2. Track Variation

The WRO 2026 rules describe different possible track configurations for the Open Challenge.

The starting section, starting zone and internal wall configuration can vary between rounds.

Because the track configuration can change, the vehicle cannot rely only on a fixed sequence of timed turns.

The autonomous system therefore needs to use sensor information to respond to the track.

## 3. Autonomous Operation

The vehicle must operate autonomously during the challenge.

The intended control process is:

1. Initialize the hardware.
2. Wait for the competition start.
3. Read sensor information.
4. Process the available sensor information.
5. Estimate the current track situation.
6. Calculate a steering command.
7. Control the propulsion system.
8. Continue navigating through the track.
9. Detect completion of the required laps.
10. Stop autonomously.

The exact implementation will be updated to match the final competition software.

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

The software generates a steering command based on the information available from the sensors.

The steering actuator then changes the direction of the steering wheels through the mechanical linkage.

The final software section will document the actual steering algorithm used by the competition program.

## 6. Drive Control

The propulsion system uses the mechanically coupled drive system described in the Motor Drive documentation.

The software controls the propulsion motors while respecting the mechanical drivetrain.

The vehicle is not controlled as an electronic left/right differential-drive system.

## 7. Corner Handling

The final control system must be able to handle both straight sections and corner sections.

The final implementation will document how the software identifies changes in the track and how steering and speed are adjusted.

Only behavior implemented in the final competition software will be described here.

## 8. Lap Completion

The Open Challenge requires three complete laps.

The final software will include a method for identifying progress through the track and determining when the required number of laps has been completed.

The exact implementation will be documented after the final program is completed.

## 9. Finish

After completing three laps, the vehicle must autonomously finish the attempt according to the competition rules.

The final documentation will explain how the software recognizes the finish condition and commands the vehicle to stop.

## 10. Development Status

The Open Challenge software is currently under development.

The strategy described in this document represents the intended architecture and does not claim that every part has already been successfully tested.

Physical test results will be added after they are actually performed.
