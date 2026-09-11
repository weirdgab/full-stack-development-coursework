hamburguer = 10.50
batata_frita = 4.00
refrigerante = 3.00

print("CARDÁPIO:")
print("Hamburguer: ", hamburguer, "R$")
print("Batata Frita: ", batata_frita, "R$")
print("Refrigerante: ", refrigerante, "R$")

quantidade_hamburguer = int(input("Digite a quanidade de hambúrgueres desejados: "))
quantidade_batata = int(input("Digite a quantidade de batatas fritas desejadas: "))
quantidade_refrigerante = int(input("Digite a quantidade de refrigerantes desejados: "))

preco_total = (hamburguer * quantidade_hamburguer) + (batata_frita * quantidade_batata) + (refrigerante * quantidade_refrigerante)

print("O preço total do seu pedido é: R$", preco_total)