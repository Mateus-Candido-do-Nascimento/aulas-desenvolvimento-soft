from menu import Menu

def exibir_menu():
    print("\n1. Adicionar Cliente")
    print("2. Adicionar Produto")
    print("3. Criar Pedido")
    print("4. Adicionar Item ao Pedido")
    print("5. Visualizar Pedido")
    print("6. Sair")

menu = Menu()

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        id_cliente = input("ID do Cliente: ")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        email = input("Email: ")
        menu.adicionar_cliente(id_cliente, nome, cpf, email)

    elif opcao == "2":
        id_produto = input("ID do Produto: ")
        nome = input("Nome: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
        menu.adicionar_produto(id_produto, nome, preco, estoque)

    elif opcao == "3":
        id_pedido = input("ID do Pedido: ")
        id_cliente = input("ID do Cliente: ")
        menu.criar_pedido(id_pedido, id_cliente)

    elif opcao == "4":
        id_pedido = input("ID do Pedido: ")
        id_produto = input("ID do Produto: ")
        quantidade = int(input("Quantidade: "))
        menu.adicionar_item_pedido(id_pedido, id_produto, quantidade)

    elif opcao == "5":
        id_pedido = input("ID do Pedido: ")
        print(menu.visualizar_pedido(id_pedido))

    elif opcao == "6":
        break

    else:
        print("Opção inválida. Tente novamente.")