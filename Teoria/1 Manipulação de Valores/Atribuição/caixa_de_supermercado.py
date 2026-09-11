detergente = 1.99
esponja = 2.0
desinfetante = 10.0

quantidade_detergente = int(input("Quantos detergentes foram comprados: "))
quantidade_esponja = int(input("Quantas esponjas foram compradas: "))
quantidade_desinfetante = int(input("Quantos desinfetantes foram comprados: "))

preco_total = (detergente * quantidade_detergente) + (esponja * quantidade_esponja) + (desinfetante * quantidade_desinfetante)

print("O preço total ficou: R$", preco_total)