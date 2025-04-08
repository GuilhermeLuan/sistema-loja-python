class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        

    def aumentar_estoque(self, quantidade):
        if quantidade <= 0:
            print("Quantidade inválida")
            return

        self.quantidade_estoque += quantidade
    
    def diminuir_estoque(self, quantidade):
        if quantidade <= 0:
            print("Quantidade inválida")
            return
        
        self.quantidade_estoque -= quantidade

    def __str__(self):
        return f"Nome: {self.nome}, Preço: R$ {self.preco}, Quantidade em Estoque: {self.quantidade_estoque}"