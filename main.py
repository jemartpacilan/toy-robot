import sys
from src.command_processor import CommandProcessor
from src.robot import Robot
from src.table import Table

if __name__ == "__main__":
    robot = Robot()
    table = Table(5, 5)
    command_processor = CommandProcessor(robot, table)

    for command in sys.stdin:
        command = command_processor.parse(command)
        if command:
            command.execute()
