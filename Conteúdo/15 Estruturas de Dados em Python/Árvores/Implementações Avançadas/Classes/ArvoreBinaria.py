import bisect


class ArvoreBinaria(object):
    def __init__(self, elemento):
        self.arvore = []
        self.addElementos(elemento)

    # Adicionar muitos elementos
    def addElementos(self, elemento):
        for i in elemento:
            if i in self:
                continue
            self.addElemento(i)

    # Adicionar um (1) elemento
    def addElemento(self, elemento):
        if elemento not in self:
            bisect.insort(self.arvore, elemento)

    # Remove um (1) elemento
    def removeElemento(self, elemento):
        try:
            self.arvore.remove(elemento)
        except ValueError:
            return False
        return True

    def __contains__(self, elemento):
        return elemento in self.arvore

    def __iter__(self):
        for elemento in self.arvore:
            yield elemento

    def __str__(self):
        return str(self.arvore)
