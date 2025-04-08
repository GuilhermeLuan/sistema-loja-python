from entities.loja import Loja
from entities.produto import Produto
from entities.carrinho import Carrinho

loja = Loja()
carrinho = Carrinho()

loja.adicionar_produto(Produto("Arroz", 10.0, 50))
loja.adicionar_produto(Produto("Feijão", 20.0, 30))
loja.adicionar_produto(Produto("Macarrão", 30.0, 20))
loja.adicionar_produto(Produto("Azeite", 40.0, 10))
loja.adicionar_produto(Produto("Açúcar", 15.0, 60))
loja.adicionar_produto(Produto("Café", 25.0, 25))
loja.adicionar_produto(Produto("Leite", 35.0, 15))
loja.adicionar_produto(Produto("Manteiga", 45.0, 5))

while True:
    try:
        print("\nMenu:")
        print("1. Visualizar produtos")
        print("2. Adicionar produto ao carrinho")
        print("3. Remover produto do carrinho")
        print("4. Visualizar itens do carrinho")
        print("5. Finalizar compra")
        print("6. Sair")

        option = input("Escolha uma opção: ")

        match option:
            case "1":
                print()
                loja.exibir_produtos()

            case "2":
                loja.exibir_produtos()

                escolha = int(input("Escolha o número do produto para adicionar ao carrinho: ")) - 1

                if escolha > (len(loja.produtos) - 1) or escolha < 0:
                    print("Produto inválido!")
                    continue

                quantidade = int(input("Digite a quantidade: "))

                if (quantidade < 0) or (quantidade > loja.produtos[escolha].quantidade_estoque):
                    print("Quantidade inválida!")
                    continue

                carrinho.adicionar_produto(loja.produtos[escolha], quantidade)

            case "3":
                if not carrinho.itens:
                    print("Carrinho está vazio!")
                    continue

                print("Itens no carrinho:")

                carrinho.exibir_itens()

                escolha = int(input("Escolha o número do produto para remover do carrinho: ")) - 1

                if escolha > (len(carrinho.itens) - 1) or escolha < 0:
                    print("Produto inválido!")
                    continue

                produto = carrinho.itens[escolha][0]
                carrinho.remover_produto(produto)

            case "4":

                if not carrinho.itens:
                    print("Carrinho está vazio!")
                    continue

                print("Itens no carrinho:")

                carrinho.exibir_itens()

                print(f"Total: R$ {carrinho.calcular_total()}")

            case "5":

                if not carrinho.itens:
                    print("Carrinho está vazio!")
                    print("Não é possível finalizar a compra.")
                    continue

                print("\nMétodos de Pagamento:")
                print("1. Dinheiro")
                print("2. Cartão de Crédito")
                print("3. Cartão de Débito")
                print("4. Pagar com PIX")
                print("5. Sair")

                metodo_pagamento = input("Escolha o método de pagamento: ")

                total = carrinho.calcular_total()
                match metodo_pagamento:
                    case "1":
                        print("Pagamento em dinheiro - 10% de desconto")
                        print("Total à pagar: R$ {:.2f}".format(total * 0.9))

                        pagamento = float(input("Digite o valor do pagamento: "))

                        if loja.pagamento_dinheiro(total, pagamento):
                            carrinho.esvaziar()
                    case "2":
                        print("Pagamento com Cartão de Crédito")
                        print("Total à pagar: R$ {:.2f}".format(total))

                        if loja.pagamento_cartao(total):
                            carrinho.esvaziar()
                    case "3":
                        print("Pagamento com Cartão de Débito")
                        print("Total à pagar: R$ {:.2f}".format(total))
                        if loja.pagamento_cartao(total):
                            carrinho.esvaziar()
                    case "4":
                        print("Pagamento com PIX - 10% de desconto")
                        print("Total à pagar: R$ {:.2f}".format(total * 0.9))

                        total = carrinho.calcular_total()
                        if loja.pagamento_pix(total):
                            carrinho.esvaziar()
                    case "5":
                        print("Cancelando pagamento...")
                    case _:
                        print("Opção inválida! Escolha uma opção válida (1-5).")

            case "6":
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida! Escolha uma opção válida (1-5).")
    except ValueError:
        print("Entrada inválida! Insira um número.")
