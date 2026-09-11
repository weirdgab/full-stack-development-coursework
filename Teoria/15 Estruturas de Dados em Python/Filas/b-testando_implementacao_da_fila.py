from Classes.classes import FilaEncadeada, No
from Métodos import insereFila

maxFila = 10
fila = [None] * maxFila
inicioFila = None
finalFila = None

e0 = No(0, 'João')
fila = FilaEncadeada(e0)

k0 = fila.busca(0)
print(k0.valor)
print(fila)

e1 = No(1, 'Maria')
fila.insere(e1)
print(fila)

e2 = No(-1, 'Ana')
fila.insere(e2)
print(fila)

e3 = No(2, 'Arthur')
fila.insere(e3)
print(fila)

k = fila.remove()
print('Nó removido: ' + k.valor)
print(fila)

# Testa para fila em alocação contígua

print(fila)
for i in range(10):
    insereFila(i)
    print(fila)
print(insereFila(11))

for i in range(10):
    print(removeFila())
print(removeFila())
