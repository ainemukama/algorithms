def angle(time_str):
    hour, minute = time_str.split(':')
    hour, minute = float(hour), float(minute)
    hour_position = 360.0*(hour + minute/60.0)/12.0
    minute_position = 360.0*minute/60.0
    a = abs(hour_position - minute_position)
    if a > 180:
        a = 360 - a
    return a

print angle('6:45')
print angle('1:30')
print angle('10:30')
