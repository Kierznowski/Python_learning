

def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    new_word = ""
    for letter in word:
        if letter != "a" and letter != "e" and letter != "i" and letter != "o" and letter != "u" and letter != "y":
            new_word = new_word + letter
    return new_word


if __name__ == "__main__":
    main()