import datetime

x = datetime.datetime(2001,5,24)
print(x)
print(x.strftime("%A"))     # weekday: thursday
y = datetime.datetime(2000,5,24)
print(y.strftime("%A"))     # weekday: Wednesday
print(y.strftime("%B"))     # Month: May
print(y.strftime("%c"))     # Local version of date and time
print(y.strftime("%x"))     # 	Local version of date
