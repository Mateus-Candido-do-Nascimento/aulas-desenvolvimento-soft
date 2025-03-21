from produto import Produto

class ItemPedido:
    def __init__(self, produto, quantidade):
        if quantidade > produto.estoque:
            raise ValueError("Quantidade solicitada maior que o estoque disponível.")
        self.produto = produto
        self.quantidade = quantidade
        produto.reduzir_estoque(quantidade)

    def calcular_total(self):
        return self.produto.preco * self.quantidade