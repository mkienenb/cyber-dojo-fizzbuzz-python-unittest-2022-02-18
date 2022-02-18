class Fizzbuzz:

    def fizzbuzz(self, number):
        result = ""
        if (number % 3) == 0:
            result = result + "Fizz"
        if (number % 5) == 0:
            result = result + "Buzz"
        if result == "":
            result = str(number)
        return result
