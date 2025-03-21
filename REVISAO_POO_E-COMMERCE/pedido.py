from item_pedido import ItemPedido

class Pedido:
    def __init__(self, id_pedido, cliente):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        item = ItemPedido(produto, quantidade)
        self.itens.append(item)

    def calcular_total(self):
        return sum(item.calcular_total() for item in self.itens)

    def resumo_pedido(self):
        return {
            "id_pedido": self.id_pedido,
            "cliente": self.cliente.pessoa.nome,
            "total": self.calcular_total(),
            "itens": [(item.produto.nome, item.quantidade) for item in self.itens]
        }