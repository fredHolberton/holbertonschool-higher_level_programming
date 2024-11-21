#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            strToPrint = "FizzBuzz"
        elif number % 3 == 0:
            strToPrint = "Fizz"
        elif number % 5 == 0:
            strToPrint = "Buzz"
        else:
            strToPrint = str(number)
        print("{}".format(strToPrint), end=' ')
