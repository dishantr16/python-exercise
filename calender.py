"""Write a Python program to print the calendar of a given month and year.

Note: Use 'calendar' module."""


import calendar

y = int(input("enter the year: "))
m = int(input("enter the month: "))

print(calendar.month(y, m))

