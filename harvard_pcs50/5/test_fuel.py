from fuel import convert, gauge

def main():
    test_convert()

def test_convert():
    assert convert("1/2") == 0.5
    assert convert("1/0") == ZeroDivisionError
    assert convert("3/2") == ValueError

if __name__ == "__main__":
    main()