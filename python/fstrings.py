#!/usr/bin/python

# Formatting with f-strings
username = "Alan"
print(f"Hello {username}")

unit_price = 49.99
quantity = 30
subtotal = quantity * unit_price
sales_tax_rate = 0.065
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
print(f"Subtotal: ${quantity * unit_price}")

# Showing dollar amounts with commas
print(f"Subtotal: ${quantity * unit_price:,}")

# Two decimal places, fixed
print(f"Subtotal: ${quantity * unit_price:,.2f}")

# Sales tax rate
print(f"Sales Tax Rate {sales_tax_rate}")

# More user friendly output for sales tax rate
print(f"Sales Tax Rate: {sales_tax_rate:,.2%} ")

# Save format string to variable
sample1 = f'Sales Tax Rate {sales_tax_rate:,.2%}'
sample2 = f"Sales Tax Rate {sales_tax_rate:,.2%}"
sample3 = f'''Sales Tax Rate {sales_tax_rate:,.2%}'''
sample4 = f"""Sales Tax Rate {sales_tax_rate:,.2%}"""
print(sample1)
print(sample2)
print(sample3)
print(sample4)

# Multiline f-strings
output = f"""
Subtotal: ${subtotal:,.2f}
Sales Tax: ${sales_tax:,.2f}
Total: ${total:,.2f}
"""
print(output)