from PIL import Image
import random
#python 3.8
#Abrir no terminal e rodar python generator-nft.py

ListaCeu = [r"C:/Users/felip/Desktop/nft/ceu/1.png",
            r"C:/Users/felip/Desktop/nft/ceu/2.png",
            r"C:/Users/felip/Desktop/nft/ceu/3.png"]

listaFundo = [r"C:/Users/felip/Desktop/nft/fundo/1.png",
              r"C:/Users/felip/Desktop/nft/fundo/2.png",
              r"C:/Users/felip/Desktop/nft/fundo/3.png"]

listaTerreno = [r"C:/Users/felip/Desktop/nft/terreno/1.png",
                r"C:/Users/felip/Desktop/nft/terreno/2.png",
                r"C:/Users/felip/Desktop/nft/terreno/3.png"]

ceu = random.choices(ListaCeu, weights = (50,30,20))[0]
fundo = random.choices(listaFundo, weights = (50,30,20))[0]
terreno = random.choices(listaTerreno, weights = (50,30,20))[0]

ceuImage = Image.open(ceu)
fundoImage = Image.open(fundo)
terrenoImage = Image.open(terreno)

montagem = Image.alpha_composite(fundoImage, ceuImage)
montagem1 = Image.alpha_composite(montagem, terrenoImage)

montagem1.show()
montagem1.save('final.png')

#ideias e sugestões:
#Verificação de Imagem repetida, 
# criar um loop para criar vários de uma vez só, 
# gerar uma lista com todas as combinações feitas
#Achar a raridade das combinações  


#rotate image
#image = img1.rotate(180,PIL.Image.NEAREST,expand=1)