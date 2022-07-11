from tkinter import Place
import unittest
from src.commands.move_command import MoveCommand
from src.commands.place_command import PlaceCommand
from src.position import Position
from src.robot import Robot
from src.table import Table


class MoveCommandTest(unittest.TestCase):
    def test_move_robot_to_east(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(1, 1, "EAST")
        PlaceCommand(robot, table, position).execute()
        MoveCommand(robot, table).execute()
        self.assertEqual(
            robot.report(),
            "2, 1, EAST",
            "Should increase the value of the x coordinate upon moving to east",
        )

    def test_move_robot_to_west(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(1, 1, "WEST")
        PlaceCommand(robot, table, position).execute()
        MoveCommand(robot, table).execute()
        self.assertEqual(
            robot.report(),
            "0, 1, WEST",
            "Should decrease the value of the x coordinate upon moving to west",
        )

    def test_move_robot_to_north(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(1, 1, "NORTH")
        PlaceCommand(robot, table, position).execute()
        MoveCommand(robot, table).execute()
        self.assertEqual(
            robot.report(),
            "1, 2, NORTH",
            "Should increase the value of the y coordinate upon moving to north",
        )

    def test_move_robot_to_south(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(1, 1, "SOUTH")
        PlaceCommand(robot, table, position).execute()
        MoveCommand(robot, table).execute()
        self.assertEqual(
            robot.report(),
            "1, 0, SOUTH",
            "Should increase the value of the y coordinate upon moving to south",
        )
