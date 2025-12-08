from dao import ClienteDAO
from models import Cliente

dao = ClienteDAO()

def menu():
    print("\n=== Sistema de Cadastro de Clientes ===")
    print("1 - Cadastrar cliente")
    print("2 - Listar todos")
    print("3 - Buscar por ID")
    print("4 - Atualizar cliente")
    print("5 - Deletar cliente")
    print("0 - Sair")
    return input("Escolha: ")

def cadastrar():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    cliente = Cliente(nome=nome, email=email, telefone=telefone)
    dao.salvar(cliente)
    print(f"Cliente cadastrado com ID {cliente.id}")

def listar():
    clientes = dao.listar_todos()
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for c in clientes:
            print(c)

def buscar():
    id = int(input("ID: "))
    cliente = dao.buscar_por_id(id)
    print(cliente if cliente else "Não encontrado.")

def atualizar():
    id = int(input("ID do cliente a atualizar: "))
    cliente = dao.buscar_por_id(id)

    if not cliente:
        print("Cliente não existe.")
        return

    print("Pressione ENTER para manter o valor atual.")
    nome = input(f"Novo nome ({cliente.nome}): ") or cliente.nome
    email = input(f"Novo email ({cliente.email}): ") or cliente.email
    telefone = input(f"Novo telefone ({cliente.telefone}): ") or cliente.telefone

    cliente.nome = nome
    cliente.email = email
    cliente.telefone = telefone

    dao.atualizar(cliente)
    print("Cliente atualizado.")

def deletar():
    id = int(input("ID: "))
    dao.deletar(id)
    print("Cliente deletado (se existia).")

def main():
    while True:
        opc = menu()
        match opc:
            case "1": cadastrar()
            case "2": listar()
            case "3": buscar()
            case "4": atualizar()
            case "5": deletar()
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    main()
