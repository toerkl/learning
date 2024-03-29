#!/usr/bin/env python3


def sorter(*args):
    """ Pass in any number of arguments separated by commas
    Inside the function, the are treated as a tuple named args """
    # Create a list from the passed in tuple
    newlist = list(args)
    # Sort and show the list
    newlist.sort()
    print(newlist)


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
    return final_list


names = ['Bosse Johansson', 'Nisse Svensson', 'Karl Karlsson']
print(alphabetize(names))
sorter('Östen', 'Achmed', 'Qvintus', 'Krulle')
