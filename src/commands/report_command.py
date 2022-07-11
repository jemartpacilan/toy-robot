from src.commands.base_command import BaseCommand


class ReportCommand(BaseCommand):
    def execute(self):
        print(self.robot.report())
