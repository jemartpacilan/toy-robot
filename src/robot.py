class Robot:
    def __init__(self):
        self.current_position = None

    def report(self):
        """
        Returns the coordinates and the direction of the robot in a readable format.
        """
        if not self.current_position:
            return "Robot was not found on the table."
        else:
            return f"{self.current_position.x}, {self.current_position.y}, {self.current_position.direction}"

    def is_placed(self):
        """
        Checks if robot is already placed on the table.
        """
        return self.current_position is not None
