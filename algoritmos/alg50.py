# numero = int(input('Informe o numero: '))

# while numero >= 1: 
#     print(numero, end=' ')
#     numero -= 1

# for i in range (numero, 0, -1):
#     print(i, end=' ')


texto1 = 'Arthur Souto'

def saudacao():
    print(f'olá{texto1} - esse texto veio da função')
    global texto2
    texto2 = 'Renan Araujo'
    print(f'Olá {texto2} - esse texto veio da função')

saudacao()
print(f'Olá {texto1} - esse texto veio da função')
print(f'Olá {texto2} - esse texto veio da função')

