from re import I


frutas = ['acerola', 'limão', 'maçã', 'banana', 'amora']


def listar_frutas():
    for i in frutas:
        print(i)


def adicionar_fruta(nome):
    frutas.append(nome)


fruta = input('Qual fruta você quer escolher? ')
adicionar_fruta(fruta)
listar_frutas()
