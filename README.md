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
The command above will run all the tests inside the "tests" directory

## Design Considerations
- The Command Pattern was implemented to handle validation, parsing, and orchestration of user commands.
- The Handling of I/O is CLI based but if there's a need to switch to file inputs/web API there would be no extensive refactoring needed due to the flexibility of the command processor class.
- Applied HashMap to route commands.
- Implemented tests for each entities of the application.

### Things I would implement in the future that are not specified in the requirements
- Add an additional command that would help users navigate the application like a "HELP" command
- Add an additional command that would let users close the application like a "QUIT" command
- Provide an option that lets the users choose whatever input handling they want (e.g. file or cli based)
- Provide clearer text to handle exceptions

## Specification

### Description
- A command line application that of a toy robot moving on a square tabletop, 
  of dimensions 5 units x 5 units.
- There are no other obstructions on the table surface.
- The robot is free to roam around the surface of the table, but must be 
  prevented from falling to destruction. Any movement that would result in the 
  robot falling from the table must be prevented, however further valid 
  movement commands must still be allowed.
- An application that can read in commands of the following form:

```
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
```

- PLACE will put the toy robot on the table in position X,Y and facing NORTH,
  SOUTH, EAST or WEST.
- The origin (0,0) can be considered to be the SOUTH WEST most corner.
- The first valid command to the robot is a PLACE command, after that, any
  sequence of commands may be issued, in any order, including another PLACE
  command. The application should discard all commands in the sequence until a
  valid PLACE command has been executed.
- MOVE will move the toy robot one unit forward in the direction it is currently
  facing.
- LEFT and RIGHT will rotate the robot 90 degrees in the specified direction
  without changing the position of the robot.
- REPORT will announce the X,Y and F of the robot. This can be in any form, but
  standard output is sufficient.
- A robot that is not on the table can choose the ignore the MOVE, LEFT, RIGHT
  and REPORT commands.
- Input can be from a file, or from standard input, as the developer chooses.
- Provide test data to exercise the application.

### Constraints
The toy robot must not fall off the table during movement. This also includes 
the initial placement of the toy robot. Any move that would cause the robot 
to fall must be ignored.

## Example Input and Output
You can see some test scenarios that can be performed on this application [here](./test_data/test_data.txt)
