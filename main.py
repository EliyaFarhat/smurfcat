import PIL
from PIL import Image
import os, sys
import random

image = Image.open('Starry-Night-canvas-Vincent-van-Gogh-New-1889.webp')

width, height = image.size



def lum(r,g,b):
    return (r * 0.299) + (g * 0.587) +(b * 0.114)

output = ""
print(width, height)

for y in range(0, height, 3):
    for x in range(0, width):
        pixel = image.getpixel((x, y))
        r, g, b = pixel[0], pixel[1], pixel[2]
        lumi = lum(r, g, b)
        if x % width == 0:
            output += "\n"
        if lumi < 10:
            output += " "
        elif lumi < 20:
            output += "`"
        elif lumi < 30:
            output += "'"
        elif lumi < 40:
            output += "."
        elif lumi < 50:
            output += '"'
        elif lumi < 60:
            output += "~"
        elif lumi < 70:
            output += "!"
        elif lumi < 80:
            output += "+"
        elif lumi < 90:
            output += ":"
        elif lumi < 100:
            output += "v"
        elif lumi < 110:
            output += "c"
        elif lumi < 120:
            output += "I"
        elif lumi < 130:
            output += "o"
        elif lumi < 140:
            output += "w"
        elif lumi < 150:
            output += "0"
        elif lumi < 160:
            output += "X"
        elif lumi < 170:
            output += "P"
        elif lumi < 180:
            output += "$"
        elif lumi < 190:
            output += "#"
        elif lumi < 200:
            output += "R"
        elif lumi < 210:
            output += "B"
        elif lumi < 255:
            output += "@"

file = open(f'{random.randint(0,9999)}.txt', 'w')
file.write(output)