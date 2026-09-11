from Classes.Animal import Animal


class Gato(Animal):

    def falar(self):
        return 'Miau!'

    def mover(self):
        return f'{self.nome} está andando.'
