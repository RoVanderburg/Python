from datetime import datetime
from datetime import timedelta
import os.path

data_obj = open("data.txt","r+")

#input and delcarations
current = datetime.now()
year = int(input("Enter year (20xx format): "))
month = int(input("Enter month (xx format): "))
day = int(input("Enter day (xx format): "))
wage = float(input("What is your current hourly wage: $"))
future = datetime(year,month,day)
dyear = 0
dmonth = 0
dday = 0

#calc work/total days/hours returns list
def hours(year,months,days):
	x = year * 365
	y = months * 30
	z = x + y + days

	rem = (z%7)
	seven = (z - rem)/7

	workdays = int((seven * 5) + rem)
	totaldays = z

	total = [workdays,(workdays*8),totaldays,(totaldays*24)]
	return total

#sorts year, month, days
if current.year == future.year:
	if current.month == future.month:
		if current.day == future.day:
			print("0 days and hours exists between dates")
		else:
			dday = future.day - current.day
			if dday <= -1:
				dday = dday * (-1)
	else:
		dmonth = future.month - current.month
		if dmonth < 0:
			dmonth = dmonth * (-1)
		dday = future.day - current.day
		if dday <= -1:
			dday = dday * (-1)
else:
	dyear = future.year - current.year

#stores returned list
usage = hours(dyear,dmonth,dday)

#outputs
print(f'\nYears: {dyear} Months: {dmonth} Days: {dday}')

print(f'\nReturn: {usage[0]} work days, {usage[1]} work hours, {usage[2]} total days, {usage[3]} total hours')

print("\nBy that time you will have made $" + str(usage[1]*wage) + " dollars")
