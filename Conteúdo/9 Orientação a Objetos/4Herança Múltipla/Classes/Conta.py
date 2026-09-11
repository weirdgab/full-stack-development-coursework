import datetime
from Classes.Extrato import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def transfereValor(self, valor):
        if self.saldo < valor:
            return 'Não existe saldo suficiente para realizar esta transferência.'
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(
                ['TRANSFERÊNCIA', valor, datetime.datetime.today()])
            return 'Transferência realizada!'

    def gerarSaldo(self):
        print(f'Conta: {self.numero}\nSaldo: R${self.saldo}\n')
