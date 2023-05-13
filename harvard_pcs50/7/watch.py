import re
import sys


def main():
    s = input("HTML: ").strip()
    print(parse(s))

def parse(s):
    matches = re.search(r"^<iframe( (.)*)? (src=\"(https|http)?):\/\/(www\.)?((.)+)\.([a-z])+(\/(.)+)?\/((.)+)(\"(.)+)?><\/iframe>$", s)
    URL = "https://youtu.be/" + matches.group(11)
    return URL



if __name__ == "__main__":)
    main()