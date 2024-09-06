# dates
from datetime import datetime

now = datetime.now()
print(now.day)
print(now.month)
print(now.year)


timestap = now.timestamp()
print(timestap)

year_2023 = datetime(2023, 10, 22)
print(year_2023)


def año_2023(date):
    print(date.year)
    print(date.month)
    print(date.day)


año_2023(now)


from datetime import time

curent_time = time(1, 1, 0)
print(curent_time.hour)
print(curent_time.minute)
print(curent_time.second)


from datetime import date

curennt_date = date.today()
print(curennt_date.year)
print(curennt_date.month)
print(curennt_date.day)
from datetime import timedelta

start_timedetla = timedelta(200, 100, 100, weeks=13)
end_timedetla = timedelta(300, 100, 100, weeks=23)
print(start_timedetla - end_timedetla)
print(start_timedetla + end_timedetla)
