import datetime


class Poupanca:
    def __init__(self, taxaRemuneracaoMes):
        self.taxaRemuneracaoMes = taxaRemuneracaoMes
        self.data_abertura = datetime.datetime.today()

    def remuneraConta(self, taxaRemuneracaoMes):  # Aplica a remuneração da conta
        self.saldo += self.saldo * self.taxaRemuneracaoMes
