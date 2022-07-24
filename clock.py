import pathlib


def change_the_hour(hour):
    if hour > 12:
        new_hour = hour - 12
        return new_hour
    else:
        return hour


def angle_of_the_hour(hour, minute):
    if hour == 12:
        angle = minute * 0.5
        return angle

    elif hour != 12:
        angle = (hour * 30) + (minute * 0.5)
        if angle <= 180:
            return angle
        elif angle > 180:
            new_angle = 360 - angle
            return new_angle


def angle_of_the_minute(hour, minute):
    if minute <= 30:
        angle = minute * 6
        return angle

    elif minute > 30:
        angle = 180 - ((minute - 30) * 6)
        return angle


def get_angle(hour, minute):
    new_hour = change_the_hour(hour)
    hour_angle = angle_of_the_hour(new_hour, minute)
    minute_angle = angle_of_the_minute(new_hour, minute)

    if hour_angle >= minute_angle:
        angle = hour_angle - minute_angle
        return angle

    elif hour_angle < minute_angle:
        angle = minute_angle - hour_angle
        return angle


file_path = pathlib.Path("time.txt")


def my_formatter(string_to_format):
    split_string = string_to_format.split(":")
    hour = split_string[0]
    minute = split_string[1]

    return (hour, minute)


with open(file_path, 'r') as file_handler:
    file_contents = file_handler.readlines()
    for read_line in file_contents:
        returned_values = my_formatter(read_line)
        hour = int(returned_values[0])
        minute = int(returned_values[1])
        print(get_angle(hour, minute))
