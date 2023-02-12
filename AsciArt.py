from PIL import Image, ImageDraw, ImageFont
import math
import tkinter
from tkinter import filedialog
import os

root = tkinter.Tk()
root.withdraw()


def search_for_file_path():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(filetypes = [('image','.jpg'), ('image','.jpeg'), ('image','.png')],
                                         parent=root, initialdir=currdir, title='Choose a photo to convert')
    return tempdir


def getChar(input:int):
    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,'. "
    charList = list(chars)
    length = len(charList)
    interval = length/256
    return charList[math.floor(input*interval)]


photo = search_for_file_path()
text_font = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)
text_file = open('output.txt', 'w')
image = Image.open(photo)
width, height = image.size
photo_size_factor = (width + height)/2
scale = 640/photo_size_factor

image = image.resize((int(scale*width), int(scale*height*0.42)), Image.Resampling.NEAREST)
width, height = image.size
pix = image.load()

outputImage = Image.new('RGB', (8 * width, 18 * height), color = (0,0,0))
draw = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r, g, b, *_ = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))
        draw.text((j*8, i*18), getChar(h), font = text_font, 
                  fill=(0, int(g * 1.5 if g * 1.5 < 256 else 256), 0))

    text_file.write('\n')

outputImage.save('matrix.png')