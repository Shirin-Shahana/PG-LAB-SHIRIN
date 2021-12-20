import datetime
t=datetime.time(22,56,44,5)          #time class(hr,min,sec,microsec)
print(t)
print("Hour",t.hour)
print("Minute",t.minute)
print("Second",t.second)
print("Microsecond",t.microsecond)

print(".............................")

d=datetime.date.today()            #date class
print(d)
td=datetime.timedelta(days=2)       #timedelta class

print(td)
d2=d+td                             #adding 2 da
print(d2)

print("d2-d=",d2-d)

#d1=datetime.date.today()

dt=datetime.datetime.combine(d,t)
print(dt)