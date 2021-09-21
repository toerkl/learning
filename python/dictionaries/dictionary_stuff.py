#!/usr/bin/env python3

people = {
    'tlindqvist': 'Tobias Lindqvist',
    'sjohansson': 'Sven Johansson',
    'bsvensson': 'Bosse Svensson',
    'nbertilsson': 'Nils Bertilsson'
}

# Print tlindqvist
print(people['tlindqvist'])

# Put person in a variable
person = 'tlindqvist'
print(people[person])

# Get length of dictionary
print(len(people))

# Check if key exists in dictionary
persons = ['tlindqvist', 'bvonfjong']
for person in persons:
    if (person in people):
        print(f"Person {people[person]} with key {person} is in dictionary.")
    else:
        print(f"Person with key {person} is not in dictionary")
