import calendar

#to print a month
"""y=2017
m=11
print(calendar.month(y,m))
print(calendar.monthcalendar(y,m))"""

#to print whole year calender
"""print(calendar.calendar(2017))"""

#to find out day on a date
"""y=2017
m=11
d=25
t=(calendar.weekday(y,m,d)) #index of day
print(calendar.day_name[t]) #day full name
print(calendar.day_abbr[t]) #day short name"""

#to check if a leap year or not
"""y=2024
y1=2025
print(calendar.isleap(y))
print(calendar.isleap(y1))"""

#to find out days in a month
"""y=2025
m=11
print(calendar.monthrange(y,m))
print(calendar.SATURDAY)
print(calendar.monthrange(y,m)[1])"""