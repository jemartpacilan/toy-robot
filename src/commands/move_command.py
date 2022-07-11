from src.commands.base_command import BaseCommand


class MoveCommand(BaseCommand):
    def execute(self):
        if self.robot.is_placed():
            new_position = self.robot.current_position.move_to(
                self.robot.current_position.direction
            )
            if self.table.is_valid_position(new_position):
                self.robot.current_position = new_position
        else:
            print("Robot was not found on the table.")
