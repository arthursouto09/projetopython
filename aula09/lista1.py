#sort ordena a lista de forma crescente
from turtle import clear


frutas = ['morango', 'maçã', 'abacaxi', 'kiwi', 'amora', 'laranja', 'bergamota']

numeros = [1, 2, 3, 12, 41, 452, 33, 523, 64, 644]

frutas.sort()
numeros.sort()

print(frutas)
print(numeros)

frutas.reverse()
numeros.reverse()
print(frutas)
print(numeros)

del frutas[0]
print(frutas)

frutas.clear()
print(frutas)