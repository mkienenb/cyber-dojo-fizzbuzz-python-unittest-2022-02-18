from numbers import Numbers
import unittest

class TestNumbers(unittest.TestCase):
    def setup(self):
        self.display_count = 0
        self.numbers = Numbers(self.display)

    def display(self, txt):
        self.display_count = self.display_count + 1

    def test_should_display_each_number(self):
        self.numbers.show_numbers(2)
        self.assertEqual(2, self.display_count)

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
