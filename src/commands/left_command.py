from src.commands.base_command import BaseCommand
from src.position import Position


class LeftCommand(BaseCommand):
    def execute(self):
        if self.robot.is_placed():
            self.robot.current_position = Position(
                self.robot.current_position.x,
                self.robot.current_position.y,
                self.robot.current_position.move_left(),
            )
        else:
            print("Robot was not found on the table.")
