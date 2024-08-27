#CRUD C=create/insert, R=read/select, U=update, D=delete
cavaleiros =['Seya', 'Shun', 'Shiryu','Yoga']
print(cavaleiros)
#adiciona um novo elemento ao final da lista
cavaleiros.append('Ikki')
print(cavaleiros)
#extentendo a lista com outra lista
cavaleiros.extend(['Shina', 'Maryn'])
print(cavaleiros)

#inserir na lista em uma posição específica
cavaleiros.insert(0, 'Athena')
print(cavaleiros)

#remove, exclui um elemento pelo valor. 
cavaleiros.remove('Shun')
print(cavaleiros)

#pop - exclui o último elemento da lista ou o índice informado
elemento = cavaleiros.pop()
cavaleiros.pop(0)
print(cavaleiros)
print(elemento)

#indice - retorna o indice da primeira ocorrência de um valor procurado
cavaleiros.pop(cavaleiros.index('Yoga'))
print(cavaleiros.index('Yoga'))

cavaleiros[cavaleiros.index('Ikki')] = 'Ikki de fenix'
print(cavaleiros)

#contabiliza  quantidade de elementos repetidos
print(cavaleiros.count('Aldebaran'))


#sort ordena a lista de forma crescente
frutas = ['morango', 'maçã', 'abacaxi', 'kiwi', 'amora', 'laranja', 'bergamota']

numeros = [1, 2, 3, 12, 41, 452, 33, 523, 64, 644]

frutas.sort()
numeros.sort()

print(frutas)
print(numeros)
