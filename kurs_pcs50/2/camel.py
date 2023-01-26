camelcase = input("CamelCase: ")

for letter in camelcase:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter, end="")
