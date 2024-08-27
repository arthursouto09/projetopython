from difflib import restore


numero1 = int(input('Informe um número:'))
numero2 = int(input('Informe um número:'))

print('A soma é: ', numero1 + numero2)

numeros =[1, 2 ,4 , 7, 32, 23, 14, 53, 541]

print(max(numeros))
print(min(numeros))
print(len(numeros))
print(sum(numeros))



media = sum(numeros) / len(numeros)
print(media)

#função com retorno
def media (numeros):  #Dentro dos parenteses é colocado os parâmetros que a função deve exercer
    resultado = sum(numeros) / len(numeros)
    return resultado

resposta = media(numeros)
print(resposta)
#Função que receb dois números e some 
def soma(a, b):
    soma = a + b
    return soma
# uso da função sem retorno
print(soma(15, 35))

#função sem retorno
def saudacao(nome):
    print(f'Olá {nome}')
#uso da função
saudacao('Arthur')



def ola(nome, mensagem = 'Olá'):
    print('mensagem, nome')
ola('Arthur', 'oi')
ola('Arthur()')

def dividir (numero1 , numero2):
    resposta = numero1 // numero2
    resto = numero1 % numero2
    return resposta, resto


divisao, resto_divisao = dividir(9, 2)
print(divisao)
print(resto_divisao)



numeros =(1, 2 ,4 , 7, 32, 23, 14, 53, 541)
print(type(numeros))


somar = lambda a, b: a + b
print(soma(10, 5))

def exibir_informacoes(*args):  #parametro posicional é apenas o valor. Se vc quiser mandar o valor sendo especificado pra que seja será um parametro nomeado 
    print('Argumentos posicionais', args) # args= argumentos que vc vai colocar. * = multiplos argumentos
    
exibir_informacoes(1,4,'arthur', 'Teste')

def exibir_informacoes2(**args):
    print('Argumentos posicionais', args)

exibir_informacoes2(nome='Arthur', idade= '30', curso= 'python')

#key:value
#chave: valor
pessoa = {
    'nome': 'Arthur',
    'idade': 21,
    'estado_civil': 'Solteiro',
    'escolaridade': 'Universitário'
}

pessoa2 = {
    'nome': 'Renan',
    'idade': 30,
    'estado_civil': 'Solteiro',
    'escolaridade': 'Formado'
}


pessoas = [{
    'nome': 'Arthur',
    'idade': 21,
    'estado_civil': 'Solteiro',
    'escolaridade': 'Universitário'
},
{
    'nome': 'Renan',
    'idade': 30,
    'estado_civil': 'Solteiro',
    'escolaridade': 'Formado'
}]

print(pessoas[1])