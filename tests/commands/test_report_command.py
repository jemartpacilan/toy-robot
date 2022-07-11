from tkinter import Place
import unittest
from src.commands.place_command import PlaceCommand
from src.commands.report_command import ReportCommand
from src.position import Position
from src.robot import Robot
from src.table import Table


class ReportCommandTest(unittest.TestCase):
    def test_report_valid_command(self):
        robot = Robot()
        table = Table(5, 5)
        position = Position(1, 1, "NORTH")
        PlaceCommand(robot, table, position).execute()
        self.assertEqual(
            robot.report(),
            "1, 1, NORTH",
            "Should match the results",
        )

    def test_report_command_before_placement(self):
        robot = Robot()
        self.assertEqual(
            robot.report(),
            "Robot was not found on the table.",
            "Should match the results",
        )
