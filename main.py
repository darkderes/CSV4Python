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


