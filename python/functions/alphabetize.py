#!/usr/bin/env python3


def alphabetize(original_list=[]):
    """ Pass any list in square brackets, display a string with items
    sorted """
    # Inside the function make a working copy of the list passed in
    sorted_list = original_list.copy()
    # Sort the working copy
    sorted_list.sort()
    # Make a new empty string for output
    final_list = ''
    # Loop through sorted list and append name and comma and space
    for name in sorted_list:
        final_list += name + ', '
    # Knock off last comma space if final list is long enough
    final_list = final_list[:-2]
    # Print the list
    print(final_list)


names = ['Bosse Johansson', 'Nisse Svensson', 'Karl Karlsson']
alphabetize(names)
