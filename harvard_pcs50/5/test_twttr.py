from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("hej") == "hj"



if __name__ == "__main__":
    main()
