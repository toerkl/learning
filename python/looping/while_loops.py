#!/usr/bin/env python3
import random


counter = 10
while counter < 20:
    print(f"Counter is {counter}")
    counter += 1

# Only print even numbers
counter = 0
while counter < 10:
    number = random.randint(1, 99)
    # Check if number is odd
    if int(number / 2) != number / 2:
        # If it's an odd number, don't print it
        continue
    # Print the even number
    print(number)
    counter += 1
