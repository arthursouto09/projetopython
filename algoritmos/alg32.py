# verfique se uam strig é um palíndromo

texto = input('Informe a sua frase: ').lower().replace(' ', '')


if texto == texto[::-1]:
    print('É um palíndromo')
else:
    print('Não é um palindromo')