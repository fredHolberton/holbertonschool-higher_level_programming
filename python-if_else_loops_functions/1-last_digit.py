#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
if number < 0:
    lastDigit = lastDigit * -1
lastMessage = ''
if int(lastDigit) > 5:
    lastMessage = "and is greater than 5"
elif int(lastDigit) == 0:
    lastMessage = "and is 0"
elif int(lastDigit) < 6:
    lastMessage = "and is less than 6 and not 0"
print("Last digit of", number, "is", lastDigit, lastMessage)
