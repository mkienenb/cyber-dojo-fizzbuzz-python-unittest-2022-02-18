from fizzbuzz import Fizzbuzz
import unittest


class TestFizzBuzz(unittest.TestCase):

    def test_should_return_number_for_integer(self):
        self.assertEqual("2", Fizzbuzz().fizzbuzz(2))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
