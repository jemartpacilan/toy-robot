import unittest
from src.position import Position


class PositionTest(unittest.TestCase):
    def test_move_to_north_position(self):
        position = Position(1, 1, "NORTH")
        new_position = position.move_to("NORTH")

        self.assertEqual(
            new_position.y,
            2,
            "Current y coordinate should be 2 after moving north",
        )

    def test_move_to_south_position(self):
        position = Position(1, 1, "SOUTH")
        new_position = position.move_to("SOUTH")

        self.assertEqual(
            new_position.y,
            0,
            "Current y coordinate should be 0 after moving south",
        )

    def test_move_to_east_position(self):
        position = Position(1, 1, "EAST")
        new_position = position.move_to("EAST")

        self.assertEqual(
            new_position.x,
            2,
            "Current x coordinate should be 2 after moving east",
        )

    def test_move_to_west_position(self):
        position = Position(1, 1, "WEST")
        new_position = position.move_to("WEST")

        self.assertEqual(
            new_position.x,
            0,
            "Current x coordinate should be 0 after moving west",
        )

    def test_north_face_to_west(self):
        position = Position(1, 1, "NORTH")
        new_direction = position.move_left()

        self.assertEqual(
            new_direction,
            "WEST",
            "Current direction should be west after rotating to the left",
        )

    def test_west_face_to_south(self):
        position = Position(1, 1, "WEST")
        new_direction = position.move_left()

        self.assertEqual(
            new_direction,
            "SOUTH",
            "Current direction should be south after rotating to the left",
        )

    def test_south_face_to_east(self):
        position = Position(1, 1, "SOUTH")
        new_direction = position.move_left()

        self.assertEqual(
            new_direction,
            "EAST",
            "Current direction should be east after rotating to the left",
        )

    def test_east_face_to_north(self):
        position = Position(1, 1, "EAST")
        new_direction = position.move_left()

        self.assertEqual(
            new_direction,
            "NORTH",
            "Current direction should be north after rotating to the left",
        )

    def test_north_face_to_east(self):
        position = Position(1, 1, "NORTH")
        new_direction = position.move_right()

        self.assertEqual(
            new_direction,
            "EAST",
            "Current direction should be east after rotating to the right",
        )

    def test_east_face_to_south(self):
        position = Position(1, 1, "EAST")
        new_direction = position.move_right()

        self.assertEqual(
            new_direction,
            "SOUTH",
            "Current direction should be south after rotating to the right",
        )

    def test_south_face_to_west(self):
        position = Position(1, 1, "SOUTH")
        new_direction = position.move_right()

        self.assertEqual(
            new_direction,
            "WEST",
            "Current direction should be west after rotating to the right",
        )

    def test_west_face_to_north(self):
        position = Position(1, 1, "WEST")
        new_direction = position.move_right()

        self.assertEqual(
            new_direction,
            "NORTH",
            "Current direction should be north after rotating to the right",
        )
