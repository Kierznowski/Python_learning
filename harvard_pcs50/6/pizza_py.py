from tabulate import tabulate
import csv
import sys


def main():

    check()

    try:
        file = open(sys.argv[1])
        readFile = csv.reader(file)
        ListOfLists = list(readFile)
    except FileNotFoundError:
        sys.exit("File does not exist")
    
    print(tabulate(ListOfLists, tablefmt="grid"))

def check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")    


if __name__ == "__main__":
    main()
