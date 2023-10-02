import math
def to_rad(degree):
    return (degree * math.pi) / 180
hour, minute = [int(i)for i in input().split(':')]
angle_for_hour = 450 - (hour % 12 * 60 + minute) / 2
angle_for_minute = 450 - (minute * 6)
x_hour = 10 + 6 * math.cos(to_rad(angle_for_hour))
y_hour = 10 + 6 * math.sin(to_rad(angle_for_hour))
x_min = 10 + 9 * math.cos(to_rad(angle_for_minute))
y_min = 10 + 9 * math.sin(to_rad(angle_for_minute))
print('%0.1f, %0.1f' % (x_hour, y_hour))
print('%0.1f, %0.1f' % (x_min, y_min))

