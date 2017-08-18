def month_length(month, year):
	if month in [4,6,9,11]:
		return 30
	if month in [1,3,5,7,8,10,12]:
		return 31
	if month == 2:
		if year % 4 != 0:
			return 28
		else:
			if year % 100 == 0:
				if year % 400 == 0:
					return 29
				else:
					return 28
			else:
				return 29


def days_to_1jan1900(date,month,year):
	days = 0
	for y in range(1900,year):
		for m in range(1,13):
			days += month_length(m,y)

	for m in range(1,month):
		days += month_length(m,year)

	days += date - 1

	return days


Sundays = 0
for year in range(1901,2001):
	for month in range(1,13):
		days = days_to_1jan1900(1,month,year)
		if days % 7 == 6:
			Sundays += 1

print Sundays