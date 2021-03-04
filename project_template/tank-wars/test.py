# from random import randint
# import math
# import numpy


# for i in range(100):
#     r = randint(0,100)
#     pixels = 200
#     x = math.log10(r)
#     x = x *10
#     x += 200
#     x = round(x, 0)
#     print(x)

from PIL import Image

image = Image.open("assets/tank.jpg")
width,height = image.size
print(width,height)