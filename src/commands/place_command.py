from src.commands.base_command import BaseCommand


class PlaceCommand(BaseCommand):
    def execute(self):
        if self.table.is_valid_position(self.position):
            self.robot.current_position = self.position
