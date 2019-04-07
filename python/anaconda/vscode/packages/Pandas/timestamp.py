import pandas as pd

year = 2018 
month = 8
day = 25
hour = 9
minute = 7
second = 43
microsecond = 23
nanosecond = 1
tz = 'America/Chicago'

obs = pd.Timestamp(year=year, month=month, day=day, hour=hour, tz=tz,
minute=minute, second=second, microsecond=microsecond, nanosecond=nanosecond)

print(obs)
print(type(obs))
    
print(obs.day_name)

a = pd.DataFrame({str(2000):[1]})

print(a)