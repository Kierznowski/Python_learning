import random


def main():
    get_level()

    i = 0
    score = 0
    while i < 10:
        chance = 3
        generate_integer(level)

        while chance > 0:
            try:
                solution = int(input(""))
            except:
                continue

            if solution != answer:
                print("EEE")
                print(c, "+", d, "= ", end="")
                chance -= 1
                continue
            else:
                score += 1
                break

        if solution != answer:
            print(answer)
            
        i += 1
    print("Score:", str(score) + "/10")



def get_level():
    while True:
        try:
            global level
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except:
            continue

def generate_integer(level):
    if level == 1:
        a = 1
        b = 9
    elif level == 2:
        a = 10
        b = 99
    else:
        a = 100
        b = 999
    
    
    global c
    global d
    c = random.randint(a, b)
    d = random.randint(a, b)
    
    global answer 
    answer = c + d
    print (str(c), "+", str(d), "= ", end="")


if __name__ == "__main__":
    main()