from b_abstractmethod import ContaCliente


class ContaComum(ContaCliente):
    def calculo_rendimento(self):
        return self.valor_investido * self.taxa_rendimento - (self.IOF + self.IR)


cc1 = ContaComum(1, 0.1, 0.25, 1000, 0.1)
print(cc1.calculo_rendimento())
