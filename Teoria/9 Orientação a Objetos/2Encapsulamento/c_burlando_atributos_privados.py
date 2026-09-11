# Burlando atributos privados.
# Python não possui atributos privados reais.
# Acesso pode ser obtido.

from Classes.Conta import Conta

conta = Conta(numero=1, saldo=1000)
saldo1 = conta._Conta__saldo
print(saldo1)

saldo2 = conta.saldo
print(saldo2)
