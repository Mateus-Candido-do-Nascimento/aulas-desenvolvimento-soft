class Produto:
    def __init__(self, id_produto, nome, preco, estoque):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def reduzir_estoque(self, quantidade):
        if quantidade > self.estoque:
            raise ValueError("Estoque insuficiente.")
        self.estoque -= quantidade