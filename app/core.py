from PIL import Image, ImageFont, ImageDraw
from resizeimage import resizeimage


def add_overlay(image_one):
    ''' img_path, img_path -> img_file

    takes in two images and returns a new image with
    the overlay chosen

    '''
    # this will need to change!!
    path = image_one

    # img properties
    color_1 = (99, 159, 249)
    color_2 = (255, 255, 255)
    w, h = 600, 600

    # opening image
    i = Image.open(path).convert('RGB')
    i = resizeimage.resize_cover(i, [w, h])

    # adding text
    draw = ImageDraw.Draw(i)
    font = ImageFont.truetype("Emilio 19.ttf", 80)
    draw.text((25, 400), "8ASE CAMP", color_1, font=font)
    draw.text((13, 400), "1", color_2, font=font)

    # figure out how to save it!
    i.save(open(str(image_one), 'wb'))
