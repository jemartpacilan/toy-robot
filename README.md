# Toy Robot Code Challenge
The application is a simulation of a toy robot moving on a 5 x 5 unit tabletop without obstructions. See specifications below for further information about this.

## Requirements
```
Python 3+
```

## Usage

To run the application:
```
python main.py
```

The command above will show a prompt:
```
Input command >>
```

Valid commands are:

| Command       | Description
| ---           | ---
| `PLACE X, Y, F` | Places robot at specific `X` and `Y` coordinates with direction `F`. E.g. `PLACE 0, 0, NORTH`.
| `LEFT`        | Rotates the robot 90 degrees to the left without changing the position of the robot.
| `RIGHT`       | Rotates the robot 90 degrees to the right without changing the position of the robot.
| `MOVE`        | Moves the toy robot one unit forward in the direction it is currently facing..
| `REPORT`      | Prints the current x and y coordinates together with the direction that the robot is currently facing.

### Testing
To run the tests:
```
python -m unittest
```

