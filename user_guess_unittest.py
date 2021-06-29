import unittest
from main import check_input


class TestUserGuess(unittest.TestCase):

    def test_register_correct_guess(self):
        self.chosen_word = "APPLE"
        self.assertTrue(check_input("A", self.chosen_word))

    def test_register_incorrect_guess(self):
        self.chosen_word = "APPLE"
        self.assertFalse(check_input("B", self.chosen_word))


if __name__ == "__main__":
    unittest.main(verbosity=2)
