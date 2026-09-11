# Realizando a composição

from cliente import Cliente
from conta_cliente_extrato import Conta

cliente1 = Cliente(cpf='123', nome='João', endereco='Rua X')
cliente2 = Cliente(cpf='456', nome='Maria', endereco='Rua W')
conta1 = Conta(clientes=[cliente1, cliente2], numero=1, saldo=2000)

conta1.depositar(1000)
conta1.sacar(1500)
conta1.extrato.extrato(conta1.numero)
