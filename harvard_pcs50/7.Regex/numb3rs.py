import re
import sys


def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))


def validate(ip):
    if re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", ip):
        a, b, c, d = ip.split(".")
        if a <= "255" and b <= "255" and c <= "255" and d <= "255":
            return True
    return False

if __name__ == "__main__":
    main()