from os import system
import time
numero = int(input('Informe um número: '))

while numero >= 1: 
    system('cls')
    print(numero)
    numero -= 1
    time.sleep(1)