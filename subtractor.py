from PIL import ImageChops, Image

class Subtractor:
    def __init__(self):
        self.images
        pass

def subtract(fp_one, fp_two, path):
    im_one = Image.open(fp_one).convert('L')
    im_two = Image.open(fp_two).convert('L')

    im = ImageChops.subtract(im_two, im_one)
    mask = im.point(lambda i: i < 128 and 255)
    fp_out = path / (fp_one.name[:3]+'.png')

    mask.save(fp_out)
    return fp_out
