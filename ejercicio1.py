# -*- coding: utf-8 -*-
"""
Created on Tue May 12 07:34:57 2020

@author: MILAGROS PC
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# imagen = cv2.imread('log_1.jpg')
# imagen_resultado = cv2.imread('log_1.jpg')
# imagen_gray = cv2.imread('log_1.jpg', cv2.IMREAD_GRAYSCALE)

imagen = cv2.imread('log_6.jpg')
imagen_resultado = cv2.imread('log_6.jpg')
imagen_gray = cv2.imread('log_6.jpg', cv2.IMREAD_GRAYSCALE)

imagen_resultado = cv2.cvtColor(imagen_resultado, cv2.COLOR_BGR2RGB)


#Implementacion de algoritmo de Operador logaritmico 

#Inicializamos los valores

#c = 40
#c = 70
#c = 90
#c = 98
#c = 30
#c = 100
#c = 105
c=110

alto, ancho = imagen_gray.shape

for x in range(alto):
    for y in range(ancho):
        operador_log = (c * (np.log10(1 + imagen_gray[x][y])))
        if(operador_log.all() > 255):
            imagen_resultado[x][y] = 255
        else:
            imagen_resultado[x][y] = operador_log
            
#-------
#porcion de codigo utilizada para encontar un mejor resultado calculando c

#Calculamos c
# c = 255 / np.log10(1 + np.max(imagen_gray))

# def operador_punto(pixel_RGB):
#     pixel = 1 + pixel_RGB
#     loga = np.log10(pixel)
#     return (c * (loga))
    

# for x in range(alto):
#     for y in range(ancho):
#         imagen_resultado[x][y] = operador_punto(imagen_gray[x][y])

#------------

plt.imshow(imagen_resultado)
plt.savefig('Imagen2_resultado0.jpg', bbox_inches='tight')