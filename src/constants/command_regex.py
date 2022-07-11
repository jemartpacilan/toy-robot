from src.constants.direction import Direction
from enum import Enum, unique


@unique
class CommandRegex(Enum):
    PLACE_CMD_PATTERN = (
        f"PLACE\s+\d+,\s?\d+,\s?({'|'.join([dir.name for dir in Direction])})$"
    )
    REPORT_CMD_PATTERN = f"REPORT"
    MOVE_CMD_PATTERN = f"MOVE"
    LEFT_CMD_PATTERN = f"LEFT"
    RIGHT_CMD_PATTERN = f"RIGHT"

    @classmethod
    def has_member_key(self, key):
        return key in self.__members__
