class Table:
    def __init__(self, length=5, width=5):
        self.length = length
        self.width = width

    def is_valid_position(self, position):
        """
        Checks if position specified is a valid movement.
        Returns True if valid. Otherwise, returns False.
        """
        contains_x = (position.x < self.length) and (position.x >= 0)
        contains_y = (position.y < self.width) and (position.y >= 0)
        return contains_x and contains_y
