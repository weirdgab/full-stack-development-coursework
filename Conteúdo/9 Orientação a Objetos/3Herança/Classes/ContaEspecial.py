from Classes.Conta import Conta
from Classes.Extrato import Extrato
import datetime


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        # super().__init__(clientes, numero, saldo) chama o construtor e inicializa os atributos herdados.
        super().__init__(clientes, numero, saldo)
        # Atributo limite exclusivo da ContaEspecial.
        self.limite = limite
        self.extrato = Extrato()

        # Polimorfismo
        # Sobrescrever o método sacar para adicionar a lógica que permite
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print(
                f'Não existe saldo suficiente conta numero {self.numero} cliente {self.clientes.cpf}')
            return False
        else:
            self.saldo -= valor
            if (self.saldo < 0):
                self.limite += self.saldo
            self.extrato.transacoes.append(
                ['SAQUE', valor, datetime.datetime.today()])
            return True

# Método depositar precisa ser reescrito para a conta especial
    def depositar(self, valor):
        pass
