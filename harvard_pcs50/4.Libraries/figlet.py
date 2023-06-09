from pyfiglet import Figlet
figlet = Figlet()
import random
import sys

list = figlet.getFonts()

if len(sys.argv) == 1:
    f = Figlet(random.choice(list))
    text = input("Text: ")
    print(f.renderText(text))
    sys.exit()

if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    if sys.argv[2] in list:
        f = Figlet(sys.argv[2])
        text = input("Text: ")
        print(f.renderText(text))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")




