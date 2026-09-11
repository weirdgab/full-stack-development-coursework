# Classe Conta

from Classes.Contadec import Contadec


def main():
    conta = Contadec(1)
    conta.saldo = 1000  # Usando o @saldo.setter
    print(f'Saldo da conta = {conta.saldo}')  # Usando o @property


if __name__ == '__main__':
    main()
