from Classes.Conta import Conta
from Classes.Poupanca import Poupanca
from Classes.ContaRemuneradaPoupanca import ContaRemuneradaPoupanca
from Classes.Cliente import Cliente

cliente1 = Cliente('123', 'João', 'Rua X')
cliente2 = Cliente('456', 'Maria', 'Rua W')

conta1 = Conta(clientes=[cliente1, cliente2], numero=1, saldo=2000)
contapoupanca1 = Poupanca(0.1)
contaremunerada1 = ContaRemuneradaPoupanca(taxaRemuneracaoMes=0.1, clientes=[
                                           cliente1], numero=5, saldo=1000)

contaremunerada1.remuneraConta()
contaremunerada1.gerarSaldo()
