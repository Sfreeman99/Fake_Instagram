from PIL import Image
from resizeimage import resizeimage


def get_images(image):
    ''' '''
    i = Image.open(image)
    i = i.convert('RGBA')
    w, h = i.size
    i = resizeimage.resize_cover(i, [200, 200])
    i = i.convert('RGBA')
    w, h = i.size
    img_data = i.getdata()
    pixel_list = list(img_data)
    # above here is opening the image data
    # Doubles the pixels in the line below
    # pixel_list.extend(list(img_data)[::-1])

    # making the new image below here
    new_img = Image.new('RGBA', (w, h))
    new_img.putdata(pixel_list)
    return new_img
    # new_img.filter(ImageFilter.EDGE_ENHANCE_MORE).show()
    # new_img_2.show()
    # Image.alpha_composite(new_img, new_img_2).show()


def add_overlay(image_one, overlay):
    ''' img_path, img_path -> img_file

    takes in two images and returns a new image with
    the overlay chosen

    '''
    new_img = get_images(image_one)
    new_img_2 = get_images(overlay)
    new_img = Image.alpha_composite(new_img, new_img_2)
    new_img = new_img.convert('RGB')
    print(type(image_one))
    new_img.save(open(str(image_one), 'wb'))
