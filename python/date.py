#!/usr/bin/env python3

import datetime as dt
# Store today's date in today.
today = dt.date.today()
# Store some other date in last_of_teens
last_of_teens = dt.date(2019, 12, 31)

print(today)
print(last_of_teens)

print(last_of_teens.month)
print(last_of_teens.day)
print(last_of_teens.year)

# Formatting dates
print(f"{last_of_teens:%A, %B %d, %Y}")

todays_date = f"{today:%m/%d/%Y}"
print(todays_date)

# Print new years eve
new_years_eve = dt.datetime(2021, 12, 31, 23, 59, 59)
print(new_years_eve)


# Experiment with timedelta objects
new_years_day = dt.date(2021, 1, 1)
duration = dt.timedelta(days=146)
print(new_years_day + duration)

start_time = dt.datetime(2019, 3, 31, 8, 0, 0)
finish_time = dt.datetime(2019, 3, 31, 14, 34, 45)
time_between = finish_time - start_time
print(time_between)
print(type(time_between))


# Calculate my age
now = dt.datetime.now()
birthdatetime = dt.datetime(1978, 2, 20, 15, 37)
age = now - birthdatetime
print(age)
print(type(age))

# days old
days_old = age.days
# years old
years_old = days_old // 365
print(years_old)

months = (days_old % 365) // 30
print(f"You are {years_old} years and {months} months old.")