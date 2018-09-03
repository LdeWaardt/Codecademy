# The datetime Library
# A lot of times you want to keep track of when something happened. We can do so in Python using datetime.

# Here we'll use datetime to print the date and time in a nice format.

# PROBLEM: Click Run to continue

from datetime import datetime
now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day
print now.year
print now.month
print now.day
print now.strftime('%B')