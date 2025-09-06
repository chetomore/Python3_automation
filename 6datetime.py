from datetime import datetime

now = datetime.now()
print("Date & time",now)
print("Date",now.date())
print("Year",now.year)
print("Month",now.month)
print("Day",now.day)
print("Hour",now.hour)
print("Minute",now.minute)


myday=datetime(2024,5,13)
print("Specified date:",myday)

print("By Default",now)
print("Format: ",now.strftime("%d/%m/%Y, %H:%M:%S"))

##parse
date_str="2025=06-09"
date_obj=datetime.strptime(date_str,"%Y=%m-%d")
print("Date object:",date_obj)

