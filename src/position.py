from src.constants.direction import Direction


class Position:
    def __init__(self, x, y, direction):
        self.x = int(x) if x is not None else None
        self.y = int(y) if y is not None else None
        self.direction = direction

    def move_to(self, direction):
        """
        Updates the coordinates of the robot based on the given direction.
        """
        options = {
            Direction.NORTH.name: self._move_to_north,
            Direction.SOUTH.name: self._move_to_south,
            Direction.WEST.name: self._move_to_west,
            Direction.EAST.name: self._move_to_east,
        }
        return options[direction]()

    def move_left(self):
        """
        Returns the new facing direction of the robot upon a 90 degree rotation to the left.
        """
        current_direction_value = Direction[self.direction].value
        calculated_dir_value = (current_direction_value - 1) % 4
        return Direction(calculated_dir_value).name

    def move_right(self):
        """
        Returns the new facing direction of the robot upon a 90 degree rotation to the right.
        """
        current_direction_value = Direction[self.direction].value
        calculated_dir_value = (current_direction_value + 1) % 4
        return Direction(calculated_dir_value).name

    def _move_to_north(self):
        return Position(self.x, self.y + 1, self.direction)

    def _move_to_south(self):
        return Position(self.x, self.y - 1, self.direction)

    def _move_to_west(self):
        return Position(self.x - 1, self.y, self.direction)

    def _move_to_east(self):
        return Position(self.x + 1, self.y, self.direction)
