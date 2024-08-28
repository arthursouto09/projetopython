numeros_pares = []

for i in range(10):
    numero = int(input(f'Digite um número {i + 1}: '))

    if numero % 2 == 0: 
        numeros_pares.append(numero)

print('Números pares: ')
for numero in numeros_pares:
    print(numero)

