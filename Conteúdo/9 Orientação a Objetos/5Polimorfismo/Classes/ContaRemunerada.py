from Classes.ContaCliente import ContaCliente

# Classe com herança de ContaCliente.


class ContaRemunerada(ContaCliente):
    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendimento)

    # Redefine o método calculo_rendimento para aplicar a taxa de rendimento sem descontar nenhum imposto.
    def calculoRendimento(self):  # (3)
        self.valor_investido += self.valor_investido * self.taxa_rendimento
