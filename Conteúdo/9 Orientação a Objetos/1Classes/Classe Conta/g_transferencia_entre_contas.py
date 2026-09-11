class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def gerar_extrato(self):
        print(f'Número: {self.numero}\nCPF: {self.cpf}\nSaldo: {self.saldo}\n')

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ('Não existe saldo suficiente.')
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ('Transferência realizada.')


def main():
    conta1 = Conta(numero=1, cpf=123, nomeTitular='João', saldo=1000)
    conta2 = Conta(numero=2, cpf=456, nomeTitular='Maria', saldo=500)

    print('Saldo antes da transferência:\n')
    print(f'Saldo da conta 1: R${conta1.saldo}')
    print(f'Saldo da conta 2: R${conta2.saldo}\n')

    conta1.transfereValor(conta2, valor=300)
    print('Saldo após a transferência:\n')
    print(f'Saldo da conta 1: R${conta1.saldo}')
    print(f'Saldo da conta 2: R${conta2.saldo}')


if __name__ == '__main__':
    main()
