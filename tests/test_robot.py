import unittest
from src.commands.move_command import MoveCommand
from src.commands.left_command import LeftCommand
from src.commands.place_command import PlaceCommand
from src.commands.right_command import RightCommand
from src.position import Position
from src.robot import Robot
from src.table import Table


class RobotTest(unittest.TestCase):
    def test_none_current_position(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(9, 1, "EAST")
        PlaceCommand(robot, table, position).execute()
        self.assertIsNone(
            robot.current_position,
            "Current position should be none due to invalid position initialization",
        )

    def test_valid_position(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(0, 1, "EAST")
        PlaceCommand(robot, table, position).execute()
        self.assertIsNotNone(
            robot.current_position,
            "Current position should not be None due to valid position initialization",
        )
        self.assertEqual(
            robot.current_position,
            position,
            "First and second value are not equal",
        )

    def test_report_before_placement(self):
        robot = Robot()
        self.assertEqual(
            robot.report(),
            "Robot was not found on the table.",
            "Should show alert that the robot was not found on the table",
        )

    def test_report_after_placement(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(0, 1, "EAST")
        PlaceCommand(robot, table, position).execute()
        self.assertEqual(
            robot.report(),
            "0, 1, EAST",
            "Should show the correct position and facing direction of the robot",
        )

    def test_robot_is_not_placed(self):
        robot = Robot()
        self.assertFalse(
            robot.is_placed(),
            "Should return False because the robot is not on the table",
        )

    def test_robot_is_placed(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(0, 1, "EAST")
        PlaceCommand(robot, table, position).execute()
        self.assertTrue(
            robot.is_placed(),
            "Should return True because the robot is already placed on the table",
        )

    def test_robot_turns_left(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(0, 1, "WEST")
        PlaceCommand(robot, table, position).execute()
        LeftCommand(robot, table, position).execute()
        self.assertEqual(
            robot.report(),
            "0, 1, SOUTH",
            "Should show the correct facing direction of the robot when turning left",
        )

    def test_robot_turns_right(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(0, 1, "WEST")
        PlaceCommand(robot, table, position).execute()
        RightCommand(robot, table, position).execute()
        self.assertEqual(
            robot.report(),
            "0, 1, NORTH",
            "Should show the correct facing direction of the robot when turning right",
        )

    def test_robot_moves_north(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(0, 1, "NORTH")
        PlaceCommand(robot, table, position).execute()
        MoveCommand(robot, table, position).execute()
        self.assertEqual(
            robot.report(),
            "0, 2, NORTH",
            "Should show the position of the robot when moving to the north direction",
        )

    def test_robot_moves_south(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(0, 2, "SOUTH")
        PlaceCommand(robot, table, position).execute()
        MoveCommand(robot, table, position).execute()
        self.assertEqual(
            robot.report(),
            "0, 1, SOUTH",
            "Should show the position of the robot when moving to the south direction",
        )

    def test_robot_moves_east(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(1, 2, "EAST")
        PlaceCommand(robot, table, position).execute()
        MoveCommand(robot, table, position).execute()
        self.assertEqual(
            robot.report(),
            "2, 2, EAST",
            "Should show the position of the robot when moving to the east direction",
        )

    def test_robot_moves_west(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(1, 2, "WEST")
        PlaceCommand(robot, table, position).execute()
        MoveCommand(robot, table, position).execute()
        self.assertEqual(
            robot.report(),
            "0, 2, WEST",
            "Should show the position of the robot when moving to the west direction",
        )
