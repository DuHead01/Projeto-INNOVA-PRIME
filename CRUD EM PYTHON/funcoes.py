import conexao
from conexao import cursor

def menu():
    while True:
        print('1 - Cadastrar Cliente')
        print('2 - Mostrar clientes')
        print('3 - Atualizar Cliente')
        print('4 - Deletar Cliente')
        print('0 - Sair')
        opcao = int(input('Escolha uma opção: '))
        match opcao:
            case 1:
                cadastrar_cliente()
            case 2:
                mostrar_clientes()
            case 3:
                atualizar_cliente()
            case 4:
                deletar_cliente()
            case 0:
                print('Saindo...')
                return False
            case _:
                print('Opção inválida!')


def cadastrar_cliente():
    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    correspondente = input('Correspondente: ')
    processoTipo = input('Tipo de processo: ')
    data = input('Data: ')
    cursor.execute("INSERT INTO cliente (nome, sobrenome, correspondente, processoTipo, data) VALUES (?, ?, ?, ?, ?)", (nome, sobrenome, correspondente, processoTipo, data))
    conexao.conn.commit()

def mostrar_clientes():
    cursor.execute("SELECT * FROM cliente")
    for linha in cursor.fetchall():
        print(linha)

def atualizar_cliente():
    id = int(input('ID do cliente: '))
    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    correspondente = input('Correspondente: ')
    processoTipo = input('Tipo de processo: ')
    data = input('Data: ')
    cursor.execute("UPDATE cliente SET nome = ?, sobrenome = ?, correspondente = ?, processoTipo = ?, data = ? WHERE id = ?", (nome, sobrenome, correspondente, processoTipo, data, id))
    conexao.conn.commit()

def deletar_cliente():
    id = int(input('ID do cliente: '))
    cursor.execute("DELETE FROM cliente WHERE id = ?", (id,))
    print('Cliente deletado com sucesso!')
    conexao.conn.commit()

menu()