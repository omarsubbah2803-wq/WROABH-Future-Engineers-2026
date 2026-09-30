# Possible Judge Questions and Answers

## Mechanical Design

### Why did you choose parallel steering?

We chose parallel steering because it provides a simpler mechanical linkage using the LEGO Technic components available to our team.

The two steering wheels are mechanically connected and move together through the steering linkage.

### What is the difference between parallel and Ackermann steering?

In parallel steering, the two steering wheels turn at approximately the same steering angle.

In Ackermann steering, the inner wheel turns through a larger angle than the outer wheel during a corner.

We considered Ackermann steering, but our current vehicle uses parallel steering.

### Why did you not use the previous design?

The previous concept used a more differential-style propulsion architecture.

The current design uses a mechanically coupled drive system and a dedicated steering mechanism.

The change was made to use a vehicle architecture that fits the WRO requirements and better matches our current mechanical design.

---

## Motor Drive

### How does the motor drive the wheels?

The Large Motor produces rotational motion.

The rotation is transferred through the gear train to the driving axle, which then rotates the drive wheels.

The basic process is:

Motor → Gear Train → Drive Axle → Wheels

### Why do you use gears?

The gear train allows us to change the relationship between motor speed and wheel speed.

A reduction can provide more torque at the output while reducing output speed.

---

## Sensors

### What does the Pixy2 do?

The Pixy2 is used as a vision sensor.

It provides visual information that can be processed by the autonomous control software.

### How is the Pixy2 connected to the EV3?

The Pixy2 communicates with the EV3 through the I2C interface.

### What does the ultrasonic sensor do?

The ultrasonic sensor measures distance.

Its final role depends on the final competition software.

---

## Software

### How does the robot make decisions?

The software reads sensor information, processes that information and generates commands for the steering and propulsion systems.

### Why does the robot need sensors?

The Open Challenge track configuration can change between rounds.

The robot therefore needs information from the current track rather than relying only on a fixed sequence of movements.

### How does the robot stop?

The final software is intended to detect completion of the required three laps and stop the vehicle autonomously.

The exact implementation will be explained using the final competition code.

---

## Development

### What was your previous design?

Our previous concept used a more differential-style propulsion approach.

The current vehicle instead uses mechanically coupled propulsion and dedicated parallel steering.

### Why did you change it?

We changed the architecture to use a dedicated steering mechanism and a mechanically coupled drive system that matches the competition vehicle requirements.

### How did you develop the robot?

Our development process follows:

Plan → Build → Test → Improve

Important design changes are documented together with their reasons and actual results.

---

## Testing

### How did you test the robot?

We will describe only tests that were actually performed.

Each test should include the robot version, objective, configuration, observed behavior and result.

### What was the most difficult problem?

The answer should describe a real problem encountered during development and the actual solution used by the team.

---

## Important Rule

All answers given to judges must describe the real robot, real software and real development process.

We should not claim a measurement, test result or software feature that has not actually been verified.
