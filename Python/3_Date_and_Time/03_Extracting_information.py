# Extracting Information
# Notice how the output looks like 2013-11-25 23:45:14.317454. What if you don't want the entire date and time?

from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

# You already have the first two lines.

#In the third line, we take the year (and only the year) from the variable now and store it in current_year.

# In the fourth and fifth lines, we store the month and day from now.

# PROBLEM: On a new line, print now.year. Make sure you do it after setting the now variable! Then, print out now.month. Finally, print out now.day.

from datetime import datetime
now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day
print now.year
print now.month
print now.day