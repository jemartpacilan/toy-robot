import unittest
from src.position import Position
from src.table import Table


class TableTest(unittest.TestCase):
    def test_valid_position(self):
        table = Table(5, 5)
        position = Position(0, 1, "EAST")
        is_valid = table.is_valid_position(position)
        self.assertTrue(is_valid, "Should return True due to valid position.")

    def test_invalid_x_coordinate(self):
        table = Table(5, 5)
        position = Position(9, 0, "EAST")
        is_valid = table.is_valid_position(position)
        self.assertFalse(is_valid, "Should return False due to invalid x coordinate.")

    def test_invalid_y_coordinate(self):
        table = Table(5, 5)
        position = Position(1, 10, "EAST")
        is_valid = table.is_valid_position(position)
        self.assertFalse(is_valid, "Should return False due to invalid y coordinate.")

    def test_invalid_x_and_y_coordinates(self):
        table = Table(5, 5)
        position = Position(10, 10, "EAST")
        is_valid = table.is_valid_position(position)
        self.assertFalse(
            is_valid, "Should return False due to invalid x and y coordinates."
        )

    def test_invalid_negative_x_coordinate(self):
        table = Table(5, 5)
        position = Position(-9, 0, "EAST")
        is_valid = table.is_valid_position(position)
        self.assertFalse(
            is_valid, "Should return False due to invalid negative x coordinate."
        )

    def test_invalid_negative_y_coordinate(self):
        table = Table(5, 5)
        position = Position(1, -10, "EAST")
        is_valid = table.is_valid_position(position)
        self.assertFalse(
            is_valid, "Should return False due to invalid negative y coordinate."
        )

    def test_invalid_negative_x_and_y_coordinates(self):
        table = Table(5, 5)
        position = Position(-10, -10, "EAST")
        is_valid = table.is_valid_position(position)
        self.assertFalse(
            is_valid, "Should return False due to invalid negative x and y coordinates."
        )
