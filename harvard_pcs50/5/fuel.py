def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))
        

def convert(fraction):
    while True:
        try:
            a, b = fraction.split("/")
            a = int(a)
            b = int(b)
            percentage = a / b
            if percentage < 1:
                return percentage
            else:
                ValueError
        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):
    if percentage >= 0.99:
        return("F")
    elif percentage <= 0.01:
        return("E")
    else:
        return(str(round(percentage * 100)) + "%")


if __name__ == "__main__":
    main()

   

