from Classes.Conta import Conta
from Classes.Poupanca import Poupanca


class ContaRemuneradaPoupanca(Conta, Poupanca):
    def __init__(self, taxaRemuneracaoMes, clientes, numero, saldo):
        # Inicializar os atributos herdados da classe Conta
        Conta.__init__(self, clientes, numero, saldo)
        # Inicializar os atributos herdados da classe Poupança
        Poupanca.__init__(self, taxaRemuneracaoMes)

    def remuneraConta(self):  # Aplica a remuneração da conta polimorfismo
        self.saldo += self.saldo * (self.taxaRemuneracaoMes / 30)
