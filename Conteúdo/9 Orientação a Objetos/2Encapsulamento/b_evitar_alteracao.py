# Como evitar alteração indevida?
# Definindo atributos públicos e privados.
# O uso de "__" indica que um atributo é privado.
# Ou seja, somente pode ser alterado por um método da classe

class Conta:
    def __init__(self, numero, saldo):
        self.__numero = numero  # Atributo privado
        self.saldo = saldo     # Atributo privado


def main():
    conta = Conta(numero=1, saldo=1000)
    saldo = conta.saldo
    print(saldo)


if __name__ == '__main__':
    main()
