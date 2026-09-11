class Conta:
    def __init__(self, numero):
        self.numero = numero
        # Note o uso de somente um "_" indicando atributo que deve ser manipulado apenas internamente.
        self._saldo = 0

    # Utilizando o decorador @property, podemos proteger os atributos e acessá-los somente por meio de métodos "decorados".
    @property  # Definindo o método decorado.
    def saldo(self):
        return self._saldo

    # O decorador @setter força todas alterações de valor dos atributos privados a passar por esses métodos.
    @saldo.setter  # Definindo método setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo inválido")
        else:
            self._saldo = saldo


def main():
    conta = Conta(1)
    conta.saldo = 1000  # Usando o @saldo.setter
    print(f'Saldo da conta = {conta.saldo}')  # Usando o @property


if __name__ == '__main__':
    main()
