def angle_of_the_hour(hour, minute):
    if hour == 12:
        angle = minute*0.5
        return angle
    
    elif hour != 12:
        angle = (hour*30) + (minute*0.5)
        if angle <= 180:
            return angle
        elif angle > 180:
            new_angle = 360 - angle
            return new_angle
    

def angle_of_the_minute(hour, minute):
    if minute <= 30:
        angle = minute*6
        return angle
    
    elif minute > 30:
        angle = 180 - ((minute-30)*6)
        return angle
    

def get_angle(hour, minute):
    hour_angle = angle_of_the_hour(hour, minute)
    minute_angle = angle_of_the_minute(hour, minute)

    if hour_angle >= minute_angle:
        angle = hour_angle - minute_angle
        return angle

    elif hour_angle < minute_angle:
        angle = minute_angle - hour_angle
        return angle

#tests
print(get_angle(12,00))
print(get_angle(12,30))
print(get_angle(6,30))
print(get_angle(12,59))
print(get_angle(12,1))

