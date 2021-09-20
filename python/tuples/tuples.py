#!/usr/bin/env python3

# Tuples are immutable lists

# To create a tuple, use parentheses instead of square brackets.
prices = (29.95, 9.98, 4.95, 79.98, 2.95)

# Print length of tuple
print(len(prices))

# Count the number an item appears
print(prices.count(4.95))

# Use in to see whether a value exists in a tuple
print(4.95 in prices)

# Get index of an item
print(prices.index(4.95))

# Loop through prices
for price in prices:
    print(f"${price:.2f}")