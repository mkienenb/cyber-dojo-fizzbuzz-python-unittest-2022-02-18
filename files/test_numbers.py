from numbers import Numbers
import unittest

class TestNumbers(unittest.TestCase):
    def setUp(self):
        self.display_count = 0
        self.displayed = []
        self.numbers = Numbers(self.display)

    def display(self, txt):
        self.display_count = self.display_count + 1
        self.displayed.append(txt)

    def test_should_display_each_number(self):
        self.numbers.show_numbers(2, self.render)
        self.assertEqual(2, self.display_count)

    def render(self, number):
        return "x" + str(number)

    def test_should_render_each_number(self):
        self.numbers.show_numbers(1, self.render)
        self.assertEqual("x1", self.displayed[0])
