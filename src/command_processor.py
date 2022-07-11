import re
from src.commands.left_command import LeftCommand
from src.commands.move_command import MoveCommand
from src.commands.place_command import PlaceCommand
from src.commands.report_command import ReportCommand
from src.commands.right_command import RightCommand
from src.constants.command import Command
from src.constants.command_regex import CommandRegex
from src.position import Position


class CommandProcessor:
    def __init__(self, robot, table):
        self.robot = robot
        self.table = table

    def parse(self, command_input):
        command_input = command_input.strip()
        command = re.split("\\W+", command_input)

        if self.verify_command(command_input):
            return self.run_command(*command)
        else:
            return False

    def verify_command(self, command_input):
        """
        Checks if the input(command) is valid based on length and regex patterns.
        """
        command = re.split("\\W+", command_input)
        command_name = f"{command[0]}_CMD_PATTERN"

        if len(command) == 0:
            return False

        if CommandRegex.has_member_key(command_name):
            if not re.match(CommandRegex[command_name].value, command_input):
                return False
            else:
                return True
        return False

    def run_command(self, command, x=None, y=None, direction=None):
        """
        Calls the appropriate command specified by the user's input.
        """
        command_options = {
            Command.PLACE.name: PlaceCommand(
                self.robot, self.table, Position(x, y, direction)
            ),
            Command.MOVE.name: MoveCommand(self.robot, self.table),
            Command.LEFT.name: LeftCommand(self.robot),
            Command.RIGHT.name: RightCommand(self.robot),
            Command.REPORT.name: ReportCommand(self.robot),
        }
        return command_options[command]
