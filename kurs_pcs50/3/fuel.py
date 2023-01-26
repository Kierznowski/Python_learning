while True:
    fraction = input("Fraction: ")

    try:
        a, b = fraction.split("/")
        a = int(a)
        b = int(b)
        percentage = a / b
        if percentage < 1:
            break
        else:
            ValueError
    except (ValueError, ZeroDivisionError):
        pass

if percentage >= 0.99:
    print("F")
elif percentage <= 0.01:
    print("E")
else:
    print(str(round(percentage * 100)) + "%")