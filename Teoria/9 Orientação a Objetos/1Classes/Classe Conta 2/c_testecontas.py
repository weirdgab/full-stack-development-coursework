# Realizando agregação
from a_conta import Conta
from b_cliente import Cliente

cliente1 = Cliente(cpf=123, nome='João', endereco='Rua 1')
cliente2 = Cliente(cpf=456, nome='Maria', endereco='Rua 2')

# Criando uma conta com dois clientes, fazendo a agregação com uma lista
conta1 = Conta(clientes=[cliente1, cliente2], numero=1, saldo=0)

conta1.gerarsaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()
