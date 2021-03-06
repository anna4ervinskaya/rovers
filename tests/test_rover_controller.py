import unittest

from rover_controller import RoverController


class TestMain(unittest.TestCase):

    def test_perform_commands(self):
        expected_result = ['1 3 N', '5 1 E']

        r_c = RoverController('tests/fixtures/input_correct.txt')
        res = r_c.perform_commands()

        self.assertEqual(res, expected_result)

    def test_is_valid_false(self):
        r_c = RoverController('tests/fixtures/input_correct.txt')
        position = {'x': 1, 'y': 2, 'f': 'N'}

        self.assertEqual(r_c.is_valid_position(position), False)

    def test_is_valid_true(self):
        r_c = RoverController('tests/fixtures/input_correct.txt')
        position = {'x': 0, 'y': 2, 'f': 'N'}

        self.assertEqual(r_c.is_valid_position(position), True)

    def test_is_valid_false_limits(self):
        r_c = RoverController('tests/fixtures/input_correct.txt')
        position = {'x': 6, 'y': 2, 'f': 'N'}

        self.assertEqual(r_c.is_valid_position(position), False)