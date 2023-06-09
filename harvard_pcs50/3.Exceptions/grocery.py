list = {}


while True:
    try:
        item = input().upper()

        if item in list:
            list[item] += 1
        else:
            list[item] = 1

    except EOFError:
        for item, amount in sorted(list.items()):
            print(amount, item)
        break
