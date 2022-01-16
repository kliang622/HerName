from imgcompare import *
from PIL import Image

#uglyplskillitwithfire2.jpeg
#uglyplskillwithfire.png

def compareImages(filename1: str, filename2: str):
    f_img = filename1
    img = Image.open(f_img)
    img = img.resize((45,39))
    img.save('../tmp/compare1.png')

    f_img = filename2
    img = Image.open(f_img)
    img = img.resize((45,39))
    img.save('../tmp/compare2.png')

    diff_percent = image_diff_percent("../tmp/compare1.png", "../tmp/compare2.png")

    return diff_percent