import sys
from PIL import Image

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments!")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments!")

    shirt = Image.open("took.png")
    photo = Image.open("before2.jpg")

    photo_width, photo_height = photo.size
    shirt_width, shirt_height = shirt.size

    new_shirt_height = int((photo_width / shirt_width) * shirt_height  + 200)
    shirt_resized = shirt.resize((photo_width, new_shirt_height))

    position = (0, photo_height - new_shirt_height)
    photo.paste(shirt_resized, position, shirt_resized)

    photo.save("final.png")
    print("Image saved as final.png")

if __name__ == "__main__":
    main()
