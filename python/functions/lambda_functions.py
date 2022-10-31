#!/usr/bin/env python3


""" Minimal syntax for defining a lambda expression
(with no name) is:
    Lambda arguments : expression
    Replace arguments with data being passed
    into the expression
    Replace expresstion with an expression (formula)
    that defines what you want the lambda to return """


names = ['Zazzlebrazzle', 'Clownburg', 'Dizzieman', 'diMarco']
# Anonymous lambda function
names.sort(key = lambda anystring : anystring.lower())
print(names)

# Lambda function named currency
currency = lambda n : f"${n:,.2f}"

# Lambda function named percent
percent = lambda n: f"{n:.2%}"

print(percent(1))
print(currency(1000000))
