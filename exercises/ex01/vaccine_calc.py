"""A vaccination calculator."""

__author__ = "730335443"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
today: datetime = datetime.today()

Population_num: int = int(input("Population: "))
Doses_given: int = int(input("Doses administered: "))
Doses_day: int = int(input("Doses per day: "))
Target_num: int = int(input("Target percent vaccinated: "))


pop_decimal: float = float(Target_num / 100)
num_needed: float = float(Population_num * pop_decimal)
still_needed: int = int(num_needed - (Doses_given / 2))
doses_needed: int = int(still_needed * 2)
days_goal_met:int = int (doses_needed / Doses_day)

future: timedelta = timedelta(days_goal_met)
day_met: datetime = today + future
date: datetime = day_met.strftime("%B %d, %Y")

target_n: str = str(Target_num)
day_: str = str(days_goal_met)
date_Y: str = str(date)

print("We will reach " + target_n + "% vaccination in " + day_ + " days " + "which falls on " + date_Y)
