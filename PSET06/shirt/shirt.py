import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    check_command_line_arg()
    #open the image
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    #open shirt
    shirtfile = Image.open("shirt.png")
    #get the size of the shirt
    size = shirtfile.size
    #resize muppet image to fit shirt
    muppet = ImageOps.fit(imagefile, size)

    #paste shirt in muppet
    muppet.paste(shirtfile, shirtfile)

    #create output image
    muppet.save(sys.argv[2])

def check_command_line_arg():
    #check how many elements in the command line
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    #print(file1[1])
    #print(file2)
    #check if it is a image file
    if check_extention(file1[1]) == False:
        sys.exit("Invalid input")
    if check_extention(file2[1]) == False:
        sys.exit("Invalid output")

    #check if extention of both files are the same
    if file1[1].lower() !=file2[1].lower():
        sys.exit("Input and output have different extensions")


def check_extention(file):
    if file in [".jpg",".jepg",".png"]:
        return True
    return False





if __name__ == "__main__":
    main()
