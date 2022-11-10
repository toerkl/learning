#!/usr/bin/env python3

import datetime as dt


# Define a class named Member for making member objects.
class Member:
    """ Create a new member. """
    free_days = 90  # Not tied to any specific object

    def __init__(self, username, fullname):
        # Define attributes and give them values.
        self.username = username
        self.fullname = fullname

        # Default date_joined to today's date
        self.date_joined = dt.date.today()
        # Set is active to True initially.
        self.is_active = True
        # Free expires
        self.free_expires = dt.date.today() + dt.timedelta(days=Member.free_days)

    def show_date_joined(self):
        return f"{self.fullname} joined on {self.date_joined}"

    def activate(self, yesno):
        """ True for active, False to make inactive """
        self.is_active = yesno

    def isactive(self):
        if self.is_active is True:
            return f"{self.fullname} is active. Free membership expires on {self.free_expires}"
        else:
            return f"{self.fullname} is inactive"


def main():
    new_guy = Member("JoRo", "Johnny Rotten")
    # Inactive Johnny Rotten
    new_guy.activate(False)
    print(new_guy.username)
    print(new_guy.show_date_joined())
    print(new_guy.isactive())
    new_guy.activate(True)
    print(new_guy.isactive())
    # Alternative way of calling the same method
    print(Member.isactive(new_guy))


if '__main__':
    main()
