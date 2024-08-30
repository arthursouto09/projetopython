#texto = 'arthur Souto Santos    '

#texto2 = texto.capitalize()
#Capitalize muda o primeiro caracter da string para maiúsculo
#print(texto.capitalize())
#print(texto2)


#lower padroniza a string em minusculo
nome = 'ArThUr SoUtO SaNTos' 
nome2 = 'arthur souto santos'
print((nome.lower))

if nome.lower() == nome2.lower():
    print('São iguais')
else: 
    print('Não são iguais')



#UPPER padroniza uma string em maiúsculo

print(nome.upper())

#replace muda um padrão de caracteres de uma string

bruxa_salem = 'coração'

#bruxa_salem2 = bruxa_salem.replace('ç', 'c') #O primeiro é usado para indicar qual caracter você quer mudar, e  o segundo indica para qual caracter que vc quer mudar
#bruxa_salem2 = bruxa_salem2.replace('ã', 'a')

print(bruxa_salem.replace('çã', 'ca'))

#strip remove caracteres em branco no final e no nício de uma string
#jack_stripador = 
#print(jack_stripador.stipador.strip())


#plit divide un sting en elementos de uma lista

#string_espalhada = 


#join transforma os elementos de uma lista em um string 
#concatena strings

nome_lista = ['arthur', 'souto', 'santos']

print(' '.join(nome_lista))

dominio = '@aluno.senai.br'
print('arthur.s.santos'.join(dominio))

#slice manipula string por indice

cidade = 'Recanto das emas, cidade do povo'

print(cidade[::-1])

palindromo = 'Arara'

if palindromo.lower() == palindromo[::-1].lower():
    print('É palindromo')
else:
    print('não é palindromo')



#questao64
