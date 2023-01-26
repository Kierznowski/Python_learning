import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
        else:
            pass
    except:
        continue

x = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            pass
        else:
            if guess < x:
                print("too small")
            elif guess > x:
                print("too large")
            else:
                print("Just right!")
                break
    except:
        continue