import sys
from PIL import Image, ImageOps
import os

input_image_name = sys.argv[1]
output_image_name = sys.argv[2]

input_image_file_type = os.path.splitext(input_image_name)[1]
output_image_file_type = os.path.splitext(output_image_name)[1]

# Too few command-line arguments
if len(sys.argv) < 3:
    exit.sys("Too few command-line arguments")

# Too many command-line arguments
if len(sys.argv) > 3:
    exit.sys("Too many command-line arguments")


# Invalid output (output not jpg jpeg png)
acceptable_image_format = [".jpg", ".JPG", ".jpeg", ".JPEG", ".png", ".PNG"]
n = 0
for i in acceptable_image_format:
    if output_image_file_type == i:
        n += 1
if n == 0:
    sys.exit("Invalid output")


# Invalid input (input not jpg jpeg png)
n = 0
for i in acceptable_image_format:
    if input_image_file_type == i:
        n += 1
if n == 0:
    exit.sys("Invalid input")


# Input and output have different extensions
if input_image_file_type != output_image_file_type:
    exit.sys("Input and output have different extensions")



try:
    input_image = Image.open(input_image_name)
    shirt_image = Image.open("shirt.png")

    shirt_image_size = shirt_image.size
    input_resize_image = ImageOps.fit(input_image, shirt_image_size)

    # overlay the shirt
    input_resize_image.paste(shirt_image, shirt_image)

    # save
    input_resize_image.save(output_image_name)

except FileNotFoundError:
    exit.sys("Input does not exist")





