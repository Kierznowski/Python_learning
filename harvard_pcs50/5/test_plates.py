from plates import is_valid

def main():
    test_len() 
    test_isalpha()
    test_zero()
    test_sign()
    test_last()

def test_len():
    assert is_valid("a") == False
    assert is_valid("aaaaaaa") == False
    assert is_valid("ssss") == True

def test_isalpha():
    assert is_valid("0drr") == False
    assert is_valid("a0bbb") == False
    assert is_valid("50cs") == False
    assert is_valid("cscs") == True

def test_zero():
    assert is_valid("cs05") == False
    assert is_valid("cs50") == True

def test_sign():
    assert is_valid("cs.d") == False
    assert is_valid("cs,5") == False
    assert is_valid("cs!5") == False

def test_last():
    assert is_valid("cs0d") == False
    assert is_valid("csd5") == True

if __name__ == "__main__":
    main()