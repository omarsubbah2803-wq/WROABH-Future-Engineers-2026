# Possible Judge Questions and Answers

## Mechanical Design

### Why did you choose parallel steering?

We chose parallel steering because it provides a simple mechanical linkage using the LEGO Technic components available to our team.

The two steering wheels are connected through the steering linkage and move together when the steering actuator changes position.

### What is the difference between parallel steering and Ackermann steering?

In parallel steering, the steering wheels are designed to turn at approximately the same angle.

In Ackermann steering, the inner wheel turns through a larger angle than the outer wheel during a turn.

We considered both approaches during development, but our current vehicle uses parallel steering.

### Why did you not use the previous design?

The previous concept used a different propulsion and steering architecture.

We changed to the current design with a mechanically connected drivetrain and dedicated steering mechanism after considering the competition requirements and the mechanical design available to our team.

---

## Motor Drive

### How does the motor drive the wheels?

The Large Motors produce rotational movement.

This rotation is transferred through the mechanical gear train to the driving axle, which then rotates the drive wheels.

The basic power flow is:

Motor → Gear Train → Drive Axle → Wheels

### Why do you use gears?

The gears transfer the motor's rotation and allow the relationship between motor speed and wheel speed to be changed.

Gear reduction can provide more output torque while reducing output speed.

This creates a trade-off between speed and torque.

---

## Sensors

### What does the Pixy2 do?

The Pixy2 is used as a vision sensor.

It provides visual information that can be processed by the autonomous control software.

### How is the Pixy2 connected to the EV3?

The Pixy2 communicates with the EV3 using the I2C interface.

### What does the ultrasonic sensor do?

The ultrasonic sensor measures distance.

Its final role depends on the final competition software.

### Why did you choose these sensors?

The sensors provide different types of information.

The Pixy2 provides visual information, while the ultrasonic sensor provides distance information.

Combining different sensor types can help the autonomous system understand the environment around the vehicle.

---

## Software

### How does the robot make decisions?

The software reads sensor information, processes the information and generates commands for the steering and propulsion systems.

### Why does the robot need sensors?

The Open Challenge track configuration can change between rounds.

The vehicle therefore needs to respond to the actual track instead of depending only on a fixed sequence of movements.

### How does the robot stop?

The final software is intended to detect completion of the required three laps and stop the vehicle autonomously.

The exact implementation will be explained using the final competition code.

---

## Competition

### What challenge are you focusing on?

Our current development focus is the Open Challenge.

The Open Challenge requires the vehicle to complete three laps autonomously.

### What makes the Open Challenge difficult?

The track configuration can change between rounds.

The internal wall configuration and starting conditions are not always identical.

Therefore, the vehicle needs to react to sensor information rather than rely only on a fixed path.

---

## Development

### How did you develop the robot?

Our development process follows:

Plan → Build → Test → Improve

We considered different mechanical concepts and selected the current architecture based on the competition requirements and the components available to our team.

### What changed from the previous design?

The main change was the move toward a mechanically connected propulsion system and a dedicated steering mechanism.

The current vehicle also uses parallel steering.

### Why is the current design different from the previous design?

The current design separates propulsion and steering into different mechanical systems.

The drive system is responsible for movement, while the steering mechanism changes the direction of the vehicle.

---

## Testing

### How did you test your robot?

Only describe tests that were actually performed.

Explain what was tested, what happened and what was changed afterward.

### What was the biggest problem during development?

Use a real problem from the project and explain how the team identified the problem and what solution was implemented.

### How did testing affect your design?

Explain only changes that were actually caused by physical testing or observed behavior.

---

## Engineering Decisions

### Why did you choose this drivetrain?

We selected a mechanically connected drivetrain so that propulsion is handled through the driving axle while steering is handled by a dedicated mechanism.

### What trade-offs did you consider?

We considered the balance between mechanical simplicity, controllability, available components, space and competition requirements.

### What would you improve next?

The answer should be based on the actual problems found during physical testing and development.

---

## Important

All answers must describe the real vehicle, real software and real development process.

We should not claim measurements, test results or software features that have not actually been verified.
