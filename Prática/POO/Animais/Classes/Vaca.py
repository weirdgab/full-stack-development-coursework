from Classes.Animal import Animal


class Vaca(Animal):

    def falar(self):
        return 'Muu!'

    def mover(self):
        return f'{self.nome} está andando.'
