from tkinter import Place
import unittest
from src.commands.move_command import MoveCommand
from src.commands.left_command import LeftCommand
from src.commands.place_command import PlaceCommand
from src.commands.report_command import ReportCommand
from src.commands.right_command import RightCommand
from src.command_processor import CommandProcessor
from src.robot import Robot
from src.table import Table


class CommandProcessorTest(unittest.TestCase):
    def test_verify_invalid_blank_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = ""
        self.assertFalse(
            command_processor.verify_command(command),
            "Should return False due to invalid command",
        )

    def test_verify_invalid_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "DUMMY COMMAND"
        self.assertFalse(
            command_processor.verify_command(command),
            "Should return False due to invalid command",
        )

    def test_verify_invalid_place_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "PLACE 1, 2"
        self.assertFalse(
            command_processor.verify_command(command),
            "Should return False due to invalid place command",
        )

    def test_verify_invalid_move_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "MOVES"
        self.assertFalse(
            command_processor.verify_command(command),
            "Should return False due to invalid move command",
        )

    def test_verify_invalid_left_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "LEFTSS"
        self.assertFalse(
            command_processor.verify_command(command),
            "Should return False due to invalid left command",
        )

    def test_verify_invalid_right_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "RIGHTS"
        self.assertFalse(
            command_processor.verify_command(command),
            "Should return False due to invalid right command",
        )

    def test_verify_invalid_report_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "REPORTS"
        self.assertFalse(
            command_processor.verify_command(command),
            "Should return False due to invalid report command",
        )

    def test_verify_valid_place_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "PLACE 1, 2, NORTH"
        self.assertTrue(
            command_processor.verify_command(command),
            "Should return True due to valid place command",
        )

    def test_verify_valid_move_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "MOVE"
        self.assertTrue(
            command_processor.verify_command(command),
            "Should return True due to valid move command",
        )

    def test_verify_valid_left_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "LEFT"
        self.assertTrue(
            command_processor.verify_command(command),
            "Should return True due to valid left command",
        )

    def test_verify_valid_right_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "RIGHT"
        self.assertTrue(
            command_processor.verify_command(command),
            "Should return True due to valid right command",
        )

    def test_verify_valid_report_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "REPORT"
        self.assertTrue(
            command_processor.verify_command(command),
            "Should return True due to valid report command",
        )

    def test_parser_invalid_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "PLA CE STESTING"
        self.assertFalse(
            command_processor.parse(command),
            "Should return False due to invalid command",
        )

    def test_parser_valid_place_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "PLACE 1,1,NORTH"
        self.assertEqual(
            type(command_processor.parse(command)),
            type(PlaceCommand()),
            "Should have the same type due to valid place command",
        )

    def test_parser_valid_move_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "MOVE"
        self.assertEqual(
            type(command_processor.parse(command)),
            type(MoveCommand()),
            "Should have the same type due to valid move command",
        )

    def test_parser_valid_left_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "LEFT"
        self.assertEqual(
            type(command_processor.parse(command)),
            type(LeftCommand()),
            "Should have the same type due to valid left command",
        )

    def test_parser_valid_right_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "RIGHT"
        self.assertEqual(
            type(command_processor.parse(command)),
            type(RightCommand()),
            "Should have the same type due to valid right command",
        )

    def test_parser_valid_report_command(self):
        robot = Robot()
        table = Table(5, 5)
        command_processor = CommandProcessor(robot, table)
        command = "REPORT"
        self.assertEqual(
            type(command_processor.parse(command)),
            type(ReportCommand()),
            "Should have the same type due to valid report command",
        )
