from pessoa import Pessoa

class Cliente:
    def __init__(self, id_cliente, pessoa):
        self.id_cliente = id_cliente
        self.pessoa = pessoa
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def listar_pedidos(self):
        return [pedido.resumo_pedido() for pedido in self.pedidos]