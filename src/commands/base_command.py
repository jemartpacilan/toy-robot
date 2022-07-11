from abc import ABC, abstractmethod


class BaseCommand(ABC):
    def __init__(self, robot=None, table=None, position=None):
        self.robot = robot
        self.table = table
        self.position = position

    @abstractmethod
    def execute(self):
        pass
