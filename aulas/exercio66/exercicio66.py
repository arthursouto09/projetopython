from os import system
import operacoes as op 
# from operacoes import menu, listar_nomes
# import operações
# import operacoes


operacao = 'sim'

while operacao == 'sim': 
    op.menu()
    opcao = int(input('Informe a ação desejada: '))

    match opcao: 
        
        case 1: 
            nome = input('Que nome deseja cadastrar: ')
            op.cadastrar_nome(nome)
        
        case 2: 
            nome = input('Que nome deseja atualizar? ')
            novo_nome = input('Qual será o novo nome? ')
        
            op.atualiza_nome(nome,novo_nome)
        
        case 3: 
            nome = input('Que nome deseja remover? ')
           
            op.exluir_nome(nome)
        
        case 4: 
            op.listar_nomes()

        case _: 
            print('Opcão inválida')

    operacao = input('Deseja realizar outra operação? ')
    system('clear')