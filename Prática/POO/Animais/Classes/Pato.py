from Classes.Animal import Animal
from Classes.Voador import Voador
from Classes.Nadador import Nadador


class Pato(Animal, Voador, Nadador):

    def falar(self):
        return 'Quack!'

    def mover(self):
        return f'{self.andar()}, {self.nadar()} e {self.voar()}'

    def andar(self):
        return f'{self.nome} está andando.'
