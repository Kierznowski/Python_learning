text = input("Input: ")

for letter in text:
    if letter != "a" and letter != "e" and letter != "i" and letter != "o" and letter != "u" and letter != "y":
        print(letter, end = "")