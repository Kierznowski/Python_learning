summ = 0
while summ < 50:
    print("Amount due:", 50 - summ)
    coin = int(input("Insert coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        summ += coin
print("Change owed:", summ - 50)