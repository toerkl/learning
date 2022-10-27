#!/usr/bin/env python

def hello(user_name):  # Practice function
    """" A docstring describing the function """
    print(f'Hello {user_name}')


def hello_default(user_name='nobody'):
    """" A function with a default parameter """
    print(f'Hello {user_name}')


def hello_first_last_number(
    first, last, number=666
):
    """ A function with a default parameter
        Default arg has to be last """

    print(f'Hello {first} {last}')
    print(f'The number is {number}')


hello('tobbe')
hello_default()
hello_first_last_number('nisse', 'larsson')

# Keywork arguments
hello_first_last_number(number=123, last='Svensson', first='Bosse')
