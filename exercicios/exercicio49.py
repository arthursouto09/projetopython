numero_maior_10 = 0

for i in range (7):
    numero = int(input('Digite um número:'))

    if numero > 10: 
        numero_maior_10 += 1

print(f'quantidade de númeors maiores que 10: {numero_maior_10}')
