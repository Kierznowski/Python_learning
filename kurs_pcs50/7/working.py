import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    isCorrectFormat = re.search(r"^(([0-9][0-2]*):?([0-5][0-9])*) (AM|PM) to (([0-9][0-2]*):?([0-5][0-9])*) (AM|PM)$", s)
    if isCorrectFormat:
        matches = isCorrectFormat.groups()
        if int(matches[1]) > 12 or int(matches[5]) > 12:
            raise ValueError("Wrong format")
        first_time = new_format(matches[1], matches[2], matches[3])
        second_time = new_format(matches[5], matches[6], matches[7])
        return first_time + " to " + second_time
    else:
        raise ValueError("Wrong format")
    
def new_format(hour, minute, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    if minute == None:
        new_minute = ":00"
        new_time = str(new_hour) + str(new_minute)
    else:
        new_time = str(new_hour) + ":" + str(minute)
    return new_time


if __name__ == "__main__":
    main()