from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_date(birth_date)
    except:
        sys.exit("Wrong format")
    date(int(year), int(month), int(day))
    diff = date.today() - date(int(year), int(month), int(day))
    minutes = diff.days*24*60
    print(p.number_to_words(minutes, andword=""), "minutes")

    

def check_date(birth_date):
    if re.search(r"^[1-2][0-9]{3}-[0-2][0-9]-[0-3][0-9]$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day


if __name__ == "__main__":
    main()