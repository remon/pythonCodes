import calendar
import datetime

#@DimaAlmasri

#return current date
now = datetime.datetime.now()
#print calendar
cal = calendar.month(now.year,now.month)
print(cal)

raw_input("Press any key to close")
