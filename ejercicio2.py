# -*- coding: utf-8 -*-
"""
Created on Tue May 12 07:34:57 2020

@author: MILAGROS PC
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread('exp_5.jpg')

imagen_resultado = cv2.imread('exp_5.jpg')

imagen_gray = cv2.imread('exp_5.jpg', cv2.IMREAD_GRAYSCALE)

imagen_resultado = cv2.cvtColor(imagen_resultado, cv2.COLOR_BGR2RGB)


#Implementacion de algoritmo de Operador logaritmico 

#Inicializamos los valores

#c = 40
#c = 70
#c = 90
#c = 100
c = 209
#c = 210


alto, ancho = imagen_gray.shape

def operador_punto(pixel_RGB):
    pixel = 1 + pixel_RGB
    loga = np.log10(pixel)
    while(loga.all() <= 255 and loga.all() > 0):
        return (c * (loga))
    


for x in range(alto):
    for y in range(ancho):
        imagen_resultado[x][y] = operador_punto(imagen_gray[x][y])
        
print(operador_punto(imagen_resultado))
plt.imshow(imagen_resultado)
plt.savefig('Imagen_resultado101.jpg', bbox_inches='tight')