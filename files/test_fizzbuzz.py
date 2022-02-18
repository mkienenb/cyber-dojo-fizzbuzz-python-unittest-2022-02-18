from fizzbuzz import Fizzbuzz
import unittest


class TestFizzBuzz(unittest.TestCase):

    def test_should_return_number_for_integer(self):
        self.assertEqual("2", Fizzbuzz().fizzbuzz(2))

    def test_should_return_fizz_for_three(self):
        self.assertEqual("Fizz", Fizzbuzz().fizzbuzz(3))

    def test_should_return_buzz_for_five(self):
        self.assertEqual("Buzz", Fizzbuzz().fizzbuzz(5))

    def test_should_return_fizz_for_multiples_of_three(self):
        self.assertEqual("Fizz", Fizzbuzz().fizzbuzz(9))

    def test_should_return_buzz_for_multiples_of_five(self):
        self.assertEqual("Buzz", Fizzbuzz().fizzbuzz(10))

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
