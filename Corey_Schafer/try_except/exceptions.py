try:
    f = open("corrupt_file.txt", "r")
    if f.name == "corrupt_file.txt":
        raise Exception
        
except FileNotFoundError:
    print("Sorry this file doesn't exist.")
except Exception:                       #na końcu jak najpierw sprawdzi błędy powyżej
    print("Sorry. Something went wrong.")
else:                                   #wykona się jak wszystko jest ok
    print(f.read())
    f.close()
finally:                                #wykona się na końcu nawet po błędach
    print("Executing finally...")