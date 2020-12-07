import unittest

from main import main


class TestMain(unittest.TestCase):

    def test_main(self):

        expected = (
            "1 3 N\n"
            "5 1 E"
        )

        result = main("tests/fixtures/input_correct.txt")

        self.assertEqual(result, expected)

    def test_main_incorrect_plateau(self):
        with self.assertRaises(ValueError) as ve:
            main("tests/fixtures/input_incorrect_plateau.txt")
            self.assertEqual(
                'Plateau limits data is not correct',
                str(ve.exception)
            )

    def test_main_incorrect_position(self):
        with self.assertRaises(ValueError) as ve:
            main("tests/fixtures/input_incorrect_position.txt")
            self.assertEqual(
                'Rover position data is not correct',
                str(ve.exception)
            )

    def test_main_incorrect_commands(self):
        with self.assertRaises(ValueError) as ve:
            main("tests/fixtures/input_incorrect_commands.txt")
            self.assertEqual(
                'Rover commands data is not correct',
                str(ve.exception)
            )

    def test_main_incorrect_paths(self):
        with self.assertRaises(ValueError) as ve:
            main("tests/fixtures/input_incorrect_paths.txt")
            self.assertEqual(
                'Rovers positions conflict',
                str(ve.exception)
            )
