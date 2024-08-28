numeros = []

for i in range(10):
    numero = float(input('Digite um número: '))
    numeros.append(numero)

media = sum(numeros) / len(numeros)

print(f'A média dos números digitados é: {media:.2f}')