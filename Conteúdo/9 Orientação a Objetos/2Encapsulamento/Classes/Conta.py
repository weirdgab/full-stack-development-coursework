class Conta:

    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(
                ['SACAR', valor, "Data", datetime.datetime.today()])
            return True

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return 'Não existe saldo suficiente.'
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(
                ['TRANSFERENCIA', valor, 'Data', datetime.datetime.today(e)])

    def gerarSaldo(self):
        print(f'Número: {self.numero}\nSaldo: {self.saldo}\n')
