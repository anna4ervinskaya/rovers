import unittest

from unittest.mock import patch, MagicMock
from rover import Rover


class TestMain(unittest.TestCase):

    @patch('rover_controller.RoverController')
    def test_rover_left(self, r_c):

        controller_ins = MagicMock()
        controller_ins.is_valid_position.return_value = True
        r_c.return_value = controller_ins

        position = ['1', '2', 'N']
        commands = 'LMLMLMLMM'
        expected_left = {'x': 1, 'y': 2, 'f': 'W'}

        r = Rover(position, commands, r_c)
        r.left()

        self.assertEqual(r.pos, expected_left)

    @patch('rover_controller.RoverController')
    def test_rover_right(self, r_c):

        controller_ins = MagicMock()
        controller_ins.is_valid_position.return_value = True
        r_c.return_value = controller_ins

        position = ['1', '2', 'N']
        commands = 'LMLMLMLMM'
        expected_right = {'x': 1, 'y': 2, 'f': 'E'}

        r = Rover(position, commands, r_c)
        r.right()

        self.assertEqual(r.pos, expected_right)

    @patch('rover_controller.RoverController')
    def test_rover_move(self, r_c):

        controller_ins = MagicMock()
        controller_ins.is_valid_position.return_value = True
        r_c.return_value = controller_ins

        position = ['1', '2', 'N']
        commands = 'LMLMLMLMM'
        expected_move = {'x': 1, 'y': 3, 'f': 'N'}

        r = Rover(position, commands, r_c)
        r.move()

        self.assertEqual(r.pos, expected_move)

    @patch('rover_controller.RoverController')
    def test_rover_execute(self, r_c):

        controller_ins = MagicMock()
        controller_ins.is_valid_position.return_value = True
        r_c.return_value = controller_ins

        position = ['1', '2', 'N']
        commands = 'LMLMLMLMM'
        expected_pos = {'x': 1, 'y': 3, 'f': 'N'}

        r = Rover(position, commands, r_c)
        r.execute_path()

        self.assertEqual(r.pos, expected_pos)
