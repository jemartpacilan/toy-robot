from tkinter import Place
import unittest
from src.commands.place_command import PlaceCommand
from src.commands.report_command import ReportCommand
from src.position import Position
from src.robot import Robot
from src.table import Table


class PlaceCommandTest(unittest.TestCase):
    def test_valid_place_command(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(1, 1, "NORTH")
        PlaceCommand(robot, table, position).execute()
        self.assertEqual(
            robot.report(),
            "1, 1, NORTH",
            "Should match the results",
        )

    def test_invalid_place_command(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(-1, 1, "NORTH")
        PlaceCommand(robot, table, position).execute()
        self.assertEqual(
            robot.report(),
            "Robot was not found on the table.",
            "Should match the results",
        )
