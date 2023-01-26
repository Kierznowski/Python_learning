list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        data = input("Date: ")
        
        
        if "/" in data:
            a, b, c = data.split("/")
            if int(a) > 12 or int(b) > 31:
                continue
            else:
                print(c + "-" + a.rjust(2, "0") + "-" + b.rjust(2, "0"))
        else:
            a, b = data.split(",")
            c, d = a.split(" ")
            if int(d) > 31:
                continue
            else:
                print(b.strip(" ") + "-", end="")
                i = 1
                for _ in list:
                    if _ == c:
                        print(str(i).rjust(2, "0"), end="")
                    i += 1
                print("-" + d.rjust(2, "0"))
        break
    except:
        pass


#YYYY-MM-DD September 8, 1636