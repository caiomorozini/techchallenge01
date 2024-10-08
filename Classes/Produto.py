class Produto:
    def __init__(self, ano, subopcao, tipo, produto, quantidade):
        self.ano = ano
        self.subopcao = subopcao
        self.tipo = tipo
        self.produto = produto
        self.quantidade = quantidade

class ProdutoImport:
    def __init__(self, ano, subopcao, pais, quantidade, valor):
        self.ano = ano
        self.subopcao = subopcao
        self.pais = pais
        self.quantidade = quantidade
        self.valor = valor