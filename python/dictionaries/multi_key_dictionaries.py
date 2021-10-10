#!/usr/bin/env python3

employees = {
    'sjohansson': {
        'name': 'Sven Johansson',
        'year_hired': 2005,
        'dob': '11/23/1989',
        'has_laptop': False
    },
    'sandersson': {
        'name': 'Sten Andersson',
        'year_hired': 2004,
        'dob': '12/13/1990',
        'has_laptop': True
    }
}

# Does sjohansson have a laptop
print(employees['sjohansson']['has_laptop'])

# Loop through dictionary to see info about each individual
for employee in employees:
    print(f"Printing info about {employee}...")
    for key, value in employees[employee].items():
        print(f"{key} = {value}")
