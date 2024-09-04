divisores = list()
contador = None


numero = int(input("Informe um número: "))

for i in range(1 , numero + 1): 
    if numero % i == 0: 
        divisores.append(i)


print(divisores)