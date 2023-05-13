def main():
    string = input("Wprowadź tekst: ")
    convert(string)

def convert(n):
   print(n.replace(":)", "\U0001F642" ).replace(":(", "\U0001F641"))

main()