from time import sleep

import pyqrcode

class Loja:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
        else:
            print("Produto não encontrado na loja.")

    def pagamento_dinheiro (self, total, pagamento):
        total = total * 0.9

        if pagamento < total:
            print("Pagamento insuficiente...")
            return False
        else:
            troco = pagamento - total
            print(f"Troco R$: {troco}")
            print("Pagamento realizado com sucesso!")
            return True

    def pagamento_pix (self, total):
        qr = pyqrcode.create(str(total))
        print(qr.terminal(quiet_zone=1))

        sleep(3)

        print("Pagamento realizado com sucesso!")
        return True

    def pagamento_cartao (self, total):
        print("Inserir ou aproximar cartão")
        print("Processando pagamento com cartão...")

        sleep(3)

        print("Pagamento realizado com sucesso!")
        return True

    def exibir_produtos(self):
        for idx, produto in enumerate(self.produtos):
            print(f"{idx + 1}. {produto.nome} - Preço: R$ {produto.preco} - Estoque: {produto.quantidade_estoque}")
