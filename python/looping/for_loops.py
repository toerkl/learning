#!/usr/bin/env/python3

for x in range(10):
    print(x)
print("First loop finished")

# Start loop at 1
for x in range(1, 10):
    print(x)
print("Second loop finished")

# Loop through a string
for x in "Torkel":
    print(x)
print("Looping through string done")

# Loop through a list
for x in ["The", "rain", "in", "Spain"]:
    print(x)
print("Looping through list done")

# Bailing out of loops
for x in range(10):
    if x == 6:
        break
    print(x)
print("The loop should not print 6")

answers = ["A", "C", "", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        break
    print(answer)
print("Loop of answers done")

# Continue the loop instead
for answer in answers:
    if answer == "":
        print("Incomplete")
        continue
    print(answer)
print("Loop of answers done")

# Nested loop
for outer in ["First", "Second", "Third"]:
    print(outer)
    # Inner loop
    for inner in range(3):
        print(inner + 1)

print("Both loops done")