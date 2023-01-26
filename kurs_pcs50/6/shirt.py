import sys
from PIL import Image, ImageOps


def main():
    check_command_line_arg()
    size = (200, 200)
    try:
        before = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("File not found")

    shirt = Image.open("D:\Downloads\shirt.png")

    size = shirt.size
    muppet = ImageOps.fit(before, size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2], format=None)

def check_command_line_arg():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".jpg" not in sys.argv[1] and ".jpg" not in sys.argv[2]:
        if ".jpeg" not in sys.argv[1] and ".jpeg" not in sys.argv[2]:
            if ".png" not in sys.argv[1] and ".png" not in sys.argv[2]:
                sys.exit("It's not a image file")
    

if __name__ == "__main__":
    main()