from bank import value

def main():
    test_bank()

def test_bank():
    assert value("hello") == "$0"
    assert value("hi") == "$20"
    assert value("t") == "$100"


if __name__ == "__main__":
    main()