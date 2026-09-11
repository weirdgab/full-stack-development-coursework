from Classes.Animal import Animal


class Cachorro(Animal):

    def falar(self):
        return 'Au!'

    def mover(self):
        return f'{self.nome} está andando.'
