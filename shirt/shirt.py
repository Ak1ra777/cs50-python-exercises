import os
import sys
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_extension = os.path.splitext(sys.argv[1])[1].lower()
    output_extension = os.path.splitext(sys.argv[2])[1].lower()

    extensions = ['.jpg', '.jpeg', '.png']

    if not input_extension in extensions:
        sys.exit("Invalid input")
    elif not output_extension in extensions:
        sys.exit("Invalid Output")
    elif not input_extension == output_extension:
        sys.exit("Input and output have different extensions")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    try:
        with Image.open(f"{input_path}") as input_img, Image.open("shirt.png") as shirt_img:
            input_img = ImageOps.fit(input_img, shirt_img.size)
            input_img.paste(shirt_img, (0,0), shirt_img)

            input_img.save(f"{output_path}")

    except FileNotFoundError:
        sys.exit("Input does not exist")




if __name__ == "__main__":
    main()
