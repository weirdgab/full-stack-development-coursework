# Usando atributos de classe

from Classes.Circulo import Circulo

# Primeiro teste
circ1 = Circulo(pontox=1, pontoy=1, raio=10)
print(circ1.totalCirculos)

# Segundo teste
circ2 = Circulo(pontox=2, pontoy=2, raio=20)
print(circ2.totalCirculos)

# Primeiro objeto instanciado é incrementado da mesma forma!
print(circ1.totalCirculos)
