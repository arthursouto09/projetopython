nomes =[]
matricula = 1


def menu():
    opcoes = ['Cadastrar nome', 'Atualizar nome', 'Excluir nome', 'Listar nomes']

    for indice ,opcao in enumerate(opcoes):
        print(f'{indice + 1} - {opcao}')


def listar_nomes():
     for indice ,nome in enumerate(nomes):
                print(f'{indice} - {nome}')

def cadastrar_nome(nome, email, data_nascimento, matricula):
    matricula += 1
    aluno= {
        'nome': nome, 
        'email': email, 
        'data_nascimento': data_nascimento, 
        'matricula': matricula}
    nomes.append(aluno)

def atualiza_nome(nome, novo_nome):
    nome[nomes.index(nome)] = novo_nome

def excluir_nome(nome):
    nomes.remove(nome)