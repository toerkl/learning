#!/usr/bin/python


def hello(user_name='nobody'):  # Practice function
    """ A dockstring describing the function """
    print(f'Hello {user_name}')


def hello_fname_lname(fname, lname, datestring=''):  # Another function
    """ A dockstring describing the function """
    msg = f'Hello {fname} {lname}.'
    if len(datestring) > 0:
        msg += f' You mentioned {datestring}'
    print(msg)


this_person = 'John Doe'
hello(this_person)
hello()


hello_fname_lname('Deja', 'Vu', '12/31/2019')
hello_fname_lname('King', 'Arthur')
