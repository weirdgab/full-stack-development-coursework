from abc import ABC, abstractmethod


class Veiculo(ABC):

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def ligar(self):
        pass


class Carro(Veiculo):

    def mover(self):
        return 'O carro está se movendo.'

    def ligar(self):
        return 'O carro está ligado.'


class Bicicleta(Veiculo):

    def mover(self):
        return 'A bicicleta está ligada.'

    def ligar(self):
        return 'A bicicleta está se movendo.'


class Aviao(Veiculo):

    def mover(self):
        return 'O Avião está voando.'

    def ligar(self):
        return 'O Avião está ligado.'


carro = Carro()
bicicleta = Bicicleta()
aviao = Aviao()

print(carro.ligar())
print(bicicleta.ligar())
print(aviao.ligar(), '\n')

print(carro.mover())
print(bicicleta.mover())
print(aviao.mover(), '\n')
