import os
import numpy as np
import cv2


"""esto crea un arreglo de 3x3 dimensiones con 0 que representa el color negro y el 255 para colores blancos , se crea un cuadro de 3x3 en 2d con numpy"""
img = np.zeros((3,3),dtype=np.uint8)
print(img)

"Let's now convert this image into blue-green-red (BGR) format using"
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
print(img.shape)

"este codigo hace un random de 120.000 Bytes"
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)

"Convertir un arreglo en una imagen de escala de grises 400x300"
grayImage = flatNumpyArray.reshape(300,400)
cv2.imwrite('RandomGray.png',grayImage)

"Convertir un arreglo en una imagen a color 400x100"
bgrImage = flatNumpyArray.reshape(100,400,3)
cv2.imwrite('RandomColor.png',bgrImage)

"Codigo edita pixel 0,0 y le coloca un color blanco"
img = cv2.imread("MyPic.png")
img[0, 0] = [255, 255, 255]

img = cv2.imread('MyPic.png')
img.itemset((150, 120, 0), 255)  # Sets the value of a pixel's blue channel
print(img.item(150, 120, 0))  # Prints the value of a pixel's blue channel

#img = cv2.imread('MyPic.png')
img[:, :, 1] = 0

#img = cv2.imread('MyPic.png')
my_roi = img[0:100, 0:100]
img[300:400, 300:400] = my_roi

"""These three properties are defined as follows:

shape: This is a tuple describing the shape of the array. For an image, it contains (in order) the height, width, and—if the image is in color—the number of channels. The length of the shape tuple is a useful way to determine whether an image is grayscale or color. For a grayscale image, we have len(shape) == 2, and for a color image, len(shape) == 3.
size: This is the number of elements in the array. In the case of a grayscale image, this is the same as the number of pixels. In the case of a BGR image, it is three times the number of pixels because each pixel is represented by three elements (B, G, and R).
dtype: This is the datatype of the array's elements. For an 8-bit-per-channel image, the datatype is numpy.uint8."""



print(img.shape)
print(img.size)
print(img.dtype)
