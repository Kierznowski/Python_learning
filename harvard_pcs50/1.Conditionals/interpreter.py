formula = input("").split(" ")

x = float(formula[0])
z = float(formula[2])

if formula[1] == "+":
    print(x + z)
elif formula[1] == "-":
    print(x - z)
elif formula[1] == "*":
    print(x * z)
elif formula[1] == "/":
    if z == 0:
        print("Nie można dzielić przez 0!")
    else:
        print(x/z)