from Classes.classes import ListaEncadeada, No

e0 = No(0, 'João')
Lista = ListaEncadeada(e0)

k0 = Lista.busca(0)
print(k0.valor)
Lista.print()

e1 = No(1, 'Maria')
Lista.insereFinal(e1)
Lista.print()

e2 = No(-1, 'Ana')
Lista.insereInicio(e2)
Lista.print()

e3 = No(2, 'Arthur')
Lista.insereOrdenada(e3)
Lista.removeLista(2)
Lista.print()
