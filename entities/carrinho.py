class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto, quantidade):
        if quantidade > produto.quantidade_estoque or quantidade < 0:
            print("Quantidade indisponível")
            return
        produto.diminuir_estoque(quantidade)
        self.itens.append((produto, quantidade))


    def remover_produto(self, produto):
        for item in self.itens:
            if item[0] == produto:
                produto.aumentar_estoque(item[1])
                self.itens.remove(item)
                return
        print("Produto não está no carrinho")

    def calcular_total(self):
        soma = 0
        for produto, quantidade in self.itens:
            soma += produto.preco * quantidade
        return soma

    def exibir_itens(self):
        for idx, (produto, quantidade) in enumerate(self.itens):
            print(f"{idx + 1}. {produto.nome} - Quantidade: {quantidade} - Preço Unitário: R$ {produto.preco}")

    def esvaziar(self):
        self.itens = []

    def verifica_se_vazio(self):
        if not self.itens:
            return True
        return False