from pyfiglet import Figlet
import random
import sys


def main():
    figlet = Figlet()
    if len(sys.argv) == 3:
        if sys.argv[1] == "--font" or sys.argv[1] == "-f":
            fonts = figlet.getFonts()
            if sys.argv[2] in fonts:
                figlet.setFont(font=sys.argv[2])
            else:
                sys.exit("Invalid Usage")
        else:
            sys.exit("Invalid Usage")

    elif len(sys.argv) == 1:
        random_font = random.choice(figlet.getFonts())
        figlet.setFont(font=random_font)
    else:
        sys.exit("Invalid Usage")

    s = input("Input: ")
    print("Output: ")
    print(figlet.renderText(s))


main()
