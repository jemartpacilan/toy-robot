from tkinter import Place
import unittest
from src.commands.left_command import LeftCommand
from src.commands.place_command import PlaceCommand
from src.position import Position
from src.robot import Robot
from src.table import Table


class LeftCommandTest(unittest.TestCase):
    def test_move_robot_from_north_to_west(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(1, 1, "NORTH")
        PlaceCommand(robot, table, position).execute()
        LeftCommand(robot).execute()
        self.assertEqual(
            robot.report(),
            "1, 1, WEST",
            "Should change the direction of the robot to west",
        )

    def test_move_robot_from_west_to_south(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(1, 1, "WEST")
        PlaceCommand(robot, table, position).execute()
        LeftCommand(robot).execute()
        self.assertEqual(
            robot.report(),
            "1, 1, SOUTH",
            "Should change the direction of the robot to south",
        )

    def test_move_robot_from_south_to_east(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(1, 1, "SOUTH")
        PlaceCommand(robot, table, position).execute()
        LeftCommand(robot).execute()
        self.assertEqual(
            robot.report(),
            "1, 1, EAST",
            "Should change the direction of the robot to east",
        )

    def test_move_robot_from_east_to_north(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(1, 1, "EAST")
        PlaceCommand(robot, table, position).execute()
        LeftCommand(robot).execute()
        self.assertEqual(
            robot.report(),
            "1, 1, NORTH",
            "Should change the direction of the robot to north",
        )
