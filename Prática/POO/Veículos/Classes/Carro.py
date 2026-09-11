from Classes.Veículo import Veiculo


class Carro(Veiculo):
    def mover(self):
        return 'O carro está se movendo.'

    def ligar(self):
        return 'O carro está ligado.'
