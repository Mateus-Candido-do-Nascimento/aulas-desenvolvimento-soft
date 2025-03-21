import json
from cliente import Cliente
from pessoa import Pessoa
from produto import Produto
from pedido import Pedido

class Menu:
    def __init__(self):
        self.clientes = {}
        self.produtos = {}
        self.pedidos = {}
        self.carregar_dados()

    def salvar_dados(self):
        dados = {
            "clientes": {id_cliente: vars(cliente.pessoa) for id_cliente, cliente in self.clientes.items()},
            "produtos": {id_produto: vars(produto) for id_produto, produto in self.produtos.items()},
            "pedidos": {id_pedido: pedido.resumo_pedido() for id_pedido, pedido in self.pedidos.items()}
        }
        with open("dados_ecommerce.json", "w") as f:
            json.dump(dados, f, indent=4)

    def carregar_dados(self):
        try:
            with open("dados_ecommerce.json", "r") as f:
                dados = json.load(f)
                for id_cliente, pessoa_data in dados.get("clientes", {}).items():
                    pessoa = Pessoa(**pessoa_data)
                    self.clientes[id_cliente] = Cliente(id_cliente, pessoa)
                for id_produto, produto_data in dados.get("produtos", {}).items():
                    self.produtos[id_produto] = Produto(**produto_data)
                for id_pedido, pedido_data in dados.get("pedidos", {}).items():
                    cliente = self.clientes[pedido_data["cliente"]]
                    pedido = Pedido(id_pedido, cliente)
                    self.pedidos[id_pedido] = pedido
        except FileNotFoundError:
            pass

    def adicionar_cliente(self, id_cliente, nome, cpf, email):
        pessoa = Pessoa(nome, cpf, email)
        self.clientes[id_cliente] = Cliente(id_cliente, pessoa)
        self.salvar_dados()

    def adicionar_produto(self, id_produto, nome, preco, estoque):
        self.produtos[id_produto] = Produto(id_produto, nome, preco, estoque)
        self.salvar_dados()

    def criar_pedido(self, id_pedido, id_cliente):
        if id_cliente in self.clientes:
            pedido = Pedido(id_pedido, self.clientes[id_cliente])
            self.pedidos[id_pedido] = pedido
            self.clientes[id_cliente].adicionar_pedido(pedido)
            self.salvar_dados()
        else:
            raise ValueError("Cliente não encontrado.")

    def adicionar_item_pedido(self, id_pedido, id_produto, quantidade):
        if id_pedido in self.pedidos and id_produto in self.produtos:
            self.pedidos[id_pedido].adicionar_item(self.produtos[id_produto], quantidade)
            self.salvar_dados()
        else:
            raise ValueError("Pedido ou produto não encontrado.")

    def visualizar_pedido(self, id_pedido):
        if id_pedido in self.pedidos:
            return self.pedidos[id_pedido].resumo_pedido()
        else:
            raise ValueError("Pedido não encontrado.")