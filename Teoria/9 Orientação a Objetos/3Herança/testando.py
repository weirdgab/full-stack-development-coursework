from Classes.Cliente import Cliente
from Classes.Conta import Conta
from Classes.ContaEspecial import ContaEspecial
from Classes.Extrato import Extrato

cliente1 = Cliente('123', 'João', 'Rua X')
cliente2 = Cliente('456', 'Maria', 'Rua W')
cliente3 = Cliente('789', 'Joana', 'Rua H')

# As três contas foram iniciadas, as contas comuns com saldo 2000 e a ContaEspecial 1000

conta1 = Conta(cliente1, 1, 2000)
conta2 = Conta(cliente2, 2, 2000)
conta3 = ContaEspecial(cliente3, 3, 1000, 2000)

# Impresso o saldo das três contas
print(
    f'Cliente: {cliente1.cpf} da conta comum {conta1.numero} possui saldo R${conta1.saldo}.\n')
print(
    f'Cliente: {cliente2.cpf} da conta comum {conta2.numero} possui saldo R${conta2.saldo}.\n')
print(f'Cliente: {cliente3.cpf} da conta especial {conta3.numero} possui saldo R${conta3.saldo} e limite R${conta3.limite}.\n')

# Depositou 500 e tentou sacar 3000 da conta comum que não terá saldo
conta2.depositar(500)

# Mensagem indicando saldo após depósito
print(
    f'Cliente: {cliente2.cpf} da conta comum {conta2.numero} possui saldo R${conta2.saldo}.\n')

conta2.sacar(3000)

# Mensagem indicando que não foi possível sacar e o saldo atual.
print(
    f'Cliente: {cliente2.cpf} da conta comum {conta2.numero} possui saldo R${conta2.saldo}.\n')

# Depositou 100 e tentou sacar 2000 da conta especial que tem limite.
conta3.depositar(100)

# Mensagem indicando saldo após depósito:
print(f'Cliente: {cliente3.cpf} da conta especial {conta3.numero} possui saldo R${conta3.saldo} e limite {conta3.limite}.\n')

conta3.sacar(2000)

# Mensagem indicando que foi possível sacar e saldo negativo:
print(f'Cliente: {cliente3.cpf} da conta especial {conta3.numero} possui saldo R${conta3.saldo} e limite R${conta3.limite}.\n')

# Tentativa de saque acima do limite:
conta3.sacar(2000)
print(f'Cliente: {cliente3.cpf} da conta comum {conta3.numero} possui saldo R${conta3.saldo} e limite R${conta3.limite}.\n')
