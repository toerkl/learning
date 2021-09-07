#!/usr/bin/env python3


nonsense = ["snuggly", "king arthur", "stuff", "whatever"]
# Print length of list
print("Length of list of nonsense: " + str(len(nonsense)))

# Add item to end of list
nonsense.append("lovely")
print(nonsense)

# Add the word "silly" to list but only if it doesn't exist
word = "silly"
if word in nonsense:
    print(f""" The word {word} already exists """)
else:
    nonsense.append("silly")
    print(f""" Word "{word}" added nicely. """)
print(nonsense)

# Insert another word at the 3rd position
nonsense.insert(3, "ridiculous")
print(nonsense)

# Change item in list
nonsense[3] = "marvellous"
print(nonsense)

# Extend a list with another list
more_nonsense = ["utter jibberish", "senseless stuff"]
nonsense.extend(more_nonsense)
print(nonsense)

# Removing list items
nonsense.remove("utter jibberish")
print(nonsense)

# Remove all occurences of an item in a list
another_list = ["A", "B", "C", "C", "C", "D"]
print(f""" Before removal of "C": {another_list} """)
while "C" in another_list:
    another_list.remove("C")
print(f""" After removal of "C": {another_list} """)
