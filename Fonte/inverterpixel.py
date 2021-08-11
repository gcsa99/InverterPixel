
import numpy as np
from PIL import Image  
from numpy import asarray

# Carregar imagem original
image = Image.open('images/original/mascote.jpg')

#informações imagem original
#tipo
print(image.format)
#tamanho
print(image.size)
#modo (RGB, L, 1, etc)
print(image.mode)
# quantidade de bits por pixel
print(image.bits)
# valores do maior e menor pixel
print(image.getextrema())

# tipo a ser invertido -> L = 8bit pixel B&W
convertedImage = image.convert('L')


# salvar a imagem convertida
convertedImage.save('images/convertido/mascote-convertido.jpg')

#carregar imagem convertida
image = Image.open('images/convertido/mascote-convertido.jpg')

#informações da imagem convertida
print(image.format)
print(image.size)
print(image.mode)
print(image.bits)
print(image.getextrema())

# converte a imagem numa matriz   
npImage = np.array(image) 
#printa a matriz
#print('\n', npImage, '\n')
    
# carrega nas variaveis o tamanho da matriz
altura, largura = npImage.shape

for linha in range(altura):
    for coluna in range(largura):
        npImage[linha, coluna] = abs(npImage[linha, coluna] - 255)

#transforma a matriz em imagem
imagemInvertida = Image.fromarray(npImage)
imagemInvertida.save('images/invertido/mascote-invertido.jpg')
