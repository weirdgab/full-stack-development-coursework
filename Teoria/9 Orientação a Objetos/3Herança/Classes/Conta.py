import datetime
from Classes.Extrato import Extrato
from Classes.Cliente import Cliente


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(
            ['DEPÓSITO', valor, datetime.datetime.today()])

    def sacar(self, valor):
        if (self.saldo) < valor:
            print(f'Não existe saldo suficiente conta numero {self.numero}')
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(
                ['SAQUE', valor, datetime.datetime.today()])
            return True

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return 'Não existe saldo suficiente para realizar esta transferência'
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(
                ['TRANSAÇÕES', valor, datetime.datetime.today()])
            return 'Transferência realizada\n'

    def gerarSaldo(self):
        print(f'Conta: {self.numero}\nSaldo: R${self.saldo}\n')
