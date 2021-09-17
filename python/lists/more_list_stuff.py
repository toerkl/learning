#!/usr/bin/env python3

import datetime as dt


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

# Remove first item
first_item = another_list.pop(0)
# Remove last item
last_item = another_list.pop()
print(f"""First item {first_item}
          and last item {last_item}
          removed: {another_list}""")

another_list = ["A", "B", "C", "C", "C", "D"]
# Use del command to delete item
del another_list[2]
print(another_list)
# Delete entire list
del another_list
# Below should render an error since list does not exist anymore
# print(another_list)

# Clear out a list
another_list = ["A", "B", "C", "C", "C", "D"]
another_list.clear()
print(f"New another list: {another_list}")

# Count how many times "C" appears in list
another_list = ["A", "B", "C", "C", "C", "D"]
print(f"Here is the list again: {another_list}")
item_to_look_for = "C"
number_of_c = another_list.count(item_to_look_for)
print(f"{item_to_look_for} occurs {number_of_c} times")

# Find list item's index, in this example "B"
index_of_b = another_list.index("B")
print(f"B is at index {index_of_b}")

# Find list items's index, in this example "Z"
look_for = "Z"
if look_for in another_list:
    print(another_list.index(look_for))
else:
    print(f"Item {look_for} does not exist")

# Sort list
unsorted_list = ["M", "N", "Y", "X", "A", "B", "C", "C", "C", "D"]
print(f"Unsorted: {unsorted_list}")
unsorted_list.sort()
print(f"Sorted: {unsorted_list}")

# Sort dates
datelist = []
datelist.append(dt.date(2020, 12, 31))
datelist.append(dt.date(2018, 2, 28))
datelist.append(dt.date(2017, 5, 13))
datelist.append(dt.date(2019, 1, 5))
datelist.sort()
print("Sorted datelist:")
# Loop through each date to make it more readable
for date in datelist:
    print(date)

# Sort dates in reverse order
print("Sorted datelist in reverse order:")
datelist.sort(reverse=True)
for date in datelist:
    print(date)

# Print a list in reverse order, not sorted
# Copy the list first
another_list_reversed = another_list.copy()
another_list_reversed.reverse()
print(f"Another list reversed: {another_list_reversed}")
