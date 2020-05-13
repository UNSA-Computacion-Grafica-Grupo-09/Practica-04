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

imagen_original = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
imagen_resultado = cv2.cvtColor(imagen_resultado, cv2.COLOR_BGR2RGB)


array_imagen = np.asarray(imagen_original)
print(array_imagen)

#Implementacion de algoritmo de Operador logaritmico 
#Inicializamos los valores

c = 70

alto, ancho, canales = imagen_original.shape

def operador_punto(pixel_RGB):
    return (c * (np.log10(1 + pixel_RGB)))

for x in range(alto):
    for y in range(ancho):
        imagen_resultado[x][y] = operador_punto(imagen_original[x][y])
        
print(operador_punto(imagen_resultado))
plt.imshow(imagen_resultado)
plt.savefig('Imagen_resultado.jpg', bbox_inches='tight')