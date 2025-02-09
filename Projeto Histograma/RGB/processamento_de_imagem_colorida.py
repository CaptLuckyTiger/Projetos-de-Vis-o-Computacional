# -*- coding: utf-8 -*-
"""Processamento de Imagem Colorida

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kiUVAnbQb6eqfS1dYyUlX93nP2Ne3yOG
"""

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Carregemtno da imagem em cor (BGR)
images = cv2.imread('imagem.jpg')

# Divindo em canais de cores
b, g, r = cv2.split(images)

# Equalização de cada canal
eq_b = cv2.equalizeHist(b)
eq_g = cv2.equalizeHist(g)
eq_r = cv2.equalizeHist(r)

# Juntando de volta para a imagem colorida
imagem_equalizada = cv2.merge((eq_b, eq_g, eq_r))

# Negativo da imagem
imagem_negativa = 255 - images

# Segmentação por intervalo de intensidade
intervalo_min = 20
intervalo_max = 120

gray_image = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
mascara = cv2.inRange(gray_image, intervalo_min, intervalo_max)

# Aplicando a mascara na imagem
masked_image = cv2.bitwise_and(images, images, mask=mascara)

# Mostrando as imagens
cv2_imshow(images)
cv2_imshow(imagem_equalizada)
cv2_imshow(imagem_negativa)
cv2_imshow(masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()