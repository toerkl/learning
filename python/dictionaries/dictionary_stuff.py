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

# Get dictionary data with get()
# Look for a person
person = 'tlindqvist'
print(people.get(person))
# Non-existent person, returns None
person = 'bvonflong'
print(people.get(person))
# Non-existent person, returns whatevva you want
print(people.get(person, 'This person does not exist you know'))

# Change the value of a key
people['bsvensson'] = 'Bertil Svensson'
print(people)

# Change the value of a key with the update method
people.update({'bsvensson':'Bengt Svensson'})
print(people)

# Add a new key, value with the update method
people.update({'landersson':'Lasse Andersson'})
print(people)

# Nice way to display what's in the dictionary
for person in people.keys():
  print(person + "=" + people[person])

# Loop through dictionary and print values
for person in people:
    print(people[person])

# Same outcome as above but slightly different
for person in people.values():
    print(person)

# Loop through keys and values at the same time by using items():
for key, value in people.items():
    print(key, "=", value)

# Copy dictionary
copy_of_people = people.copy()
print(copy_of_people)

# Delete directory items
print(copy_of_people)
del copy_of_people["tlindqvist"]
print(copy_of_people)

# Use pop to remove item and store in variable
adios = copy_of_people.pop("landersson")
# Print dictionary without "landersson"
print(copy_of_people)
# Print name of removed person
print(adios)
# Remove last person in the dict
adios = copy_of_people.popitem()
print(copy_of_people)
print(adios)

# Clear the whole dictionary
copy_of_people.clear()
print(copy_of_people)

# Delete whole dictionary
del copy_of_people


