from Classes.ContaCliente import ContaCliente

# Classe com herança de ContaCliente.


class ContaComum(ContaCliente):
    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendimento)

    # Redefine o método cálculo_rendimento para aplicar a taxa de rendimento e descontar apenas o IOF.
    def calculoRendimento(self):  # (2)
        remuneracao = self.valor_investido * self.taxa_rendimento
        valorIOF = remuneracao * self.IOF
        self.valor_investido += remuneracao - valorIOF
