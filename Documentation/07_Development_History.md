velopment History

## 1. Engineering Process

Our robot was developed through an iterative engineering process.

Our general approach is:

Plan → Build → Evaluate → Improve

Instead of treating the first design as final, we considered different mechanical approaches and selected the architecture that best matched our competition requirements and available components.

The purpose of this section is to document how the current vehicle developed from earlier ideas into the present design.

---

## 2. Previous Vehicle Concept

Before the current vehicle was selected, our team worked on an earlier robot concept.

The previous concept had a different mechanical arrangement from the current vehicle and was based on a different approach to propulsion and steering.

The earlier design helped us identify the mechanical and control requirements that were important for the final vehicle.

It also helped us understand which parts of the design needed to be changed before competition.

---

## 3. Why We Did Not Continue With the Previous Design

We decided not to continue with the previous design after reviewing the competition requirements and the mechanical architecture we wanted for the final vehicle.

One important consideration was the WRO Future Engineers 2026 requirement for a four-wheeled vehicle with one driving axle and one steering actuator.

The rules also prohibit a differential-wheeled base and the use of an electronic differential with one motor per side.

Because of these requirements, we moved toward a mechanically connected drive system with a dedicated steering mechanism.

The previous concept was therefore treated as an earlier development stage rather than the final competition architecture.

---

## 4. Current Vehicle Design

The current vehicle uses:

- Four wheels
- A mechanically connected drive system
- A dedicated steering mechanism
- Parallel steering
- LEGO Mindstorms EV3 controller
- LEGO Large Motors
- Pixy2 camera
- Ultrasonic sensor

The current architecture separates the main vehicle functions:

- Propulsion moves the vehicle.
- Steering changes its direction.
- Sensors provide information.
- The EV3 controller processes information and controls the vehicle.

---

## 5. Change to Parallel Steering

One of the important design decisions was the choice of parallel steering.

We considered the difference between parallel steering and Ackermann steering.

In parallel steering, the steering wheels turn together at approximately the same angle.

In Ackermann steering, the inner and outer wheels use different steering angles during a turn.

Our current vehicle uses parallel steering because its mechanical linkage is simpler to implement with the LEGO Technic components available to our team.

The mechanism also gives us a direct mechanical connection between the steering actuator and the steering wheels.

---

## 6. Development of the Drive System

The propulsion system was developed around a mechanically connected drivetrain.

The motors provide rotational movement, which is transferred through the mechanical drivetrain to the driving axle and wheels.

The design separates propulsion from steering instead of using the propulsion system itself to create turning by independently controlling opposite sides of the vehicle.

This makes the mechanical functions easier to identify and document as separate subsystems.

---

## 7. Engineering Decisions

The main engineering decisions made during development were influenced by:

- WRO vehicle requirements
- Mechanical simplicity
- Available LEGO Technic components
- Steering architecture
- Drivetrain architecture
- Sensor placement
- Space available on the vehicle
- The need for autonomous control

The current design represents the architecture selected by our team after considering these factors.

---

## 8. Iteration

The project is being developed through multiple stages.

For each significant change, we aim to record:

### Problem
What problem or limitation was identified?

### Change
What was changed in the robot?

### Reason
Why was this change selected?

### Result
What happened after the change?

### Next Step
What should be improved next?

This structure allows the repository to show the engineering process rather than only the final robot.

---

## 9. Current Status

The current mechanical vehicle has been assembled.

The current steering design is parallel steering.

The vehicle uses a mechanically connected drive system and the planned sensing system includes the Pixy2 camera and ultrasonic sensor.

The final competition software is still under development.

Further changes and physical test results will be added as they are actually completed.

---

## 10. Development Principle

The team aims to improve the vehicle through practical engineering decisions rather than changing components without a reason.

When a design is changed, the reason for the change should be documented.

Future versions of the vehicle and software will be recorded in this development history as the project progresses
