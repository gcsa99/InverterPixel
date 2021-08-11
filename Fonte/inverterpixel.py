
import numpy as np
from PIL import Image  
from numpy import asarray

from APIdownload import carregarImagem

pesquisa=input()
# Carregar imagem original
#image = Image.open('images/mascote.jpg')
#image = Image.open('images/meme.jpg')
#image = Image.open('images/sapo.jpg')
image = Image.open(carregarImagem(pesquisa))

#informações imagem original
#tipo
print(image.format)
#tamanho
print(image.size)
#modo (RGB, L, 1, etc)
print(image.mode)
# quantidade de bits por pixel
#batataprint(image.bits)
# valores do maior e menor pixel
print(image.getextrema())

# tipo a ser invertido -> L = 8bit pixel B&W
convertedImage = image.convert('L')


# salvar a imagem convertida
#convertedImage.save('images/mascote-convertido.jpg')
#convertedImage.save('images/meme-convertido.jpg')
#convertedImage.save('images/sapo-convertido.jpg')
convertedImage.save('images/'+pesquisa+'-convertido.jpg')

#carregar imagem convertida
#image = Image.open('images/mascote-convertido.jpg')
#image = Image.open('images/meme-convertido.jpg')
#image = Image.open('images/sapo-convertido.jpg')
image = Image.open('images/'+pesquisa+'-convertido.jpg')


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
#imagemInvertida.save('images/mascote-invertido.jpg')
#imagemInvertida.save('images/meme-invertido.jpg')
#imagemInvertida.save('images/sapo-invertido.jpg')
imagemInvertida.save('images/'+pesquisa+'-invertido.jpg')