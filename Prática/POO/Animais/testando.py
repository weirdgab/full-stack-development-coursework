from Classes.Animal import Animal
from Classes.Cachorro import Cachorro
from Classes.Gato import Gato
from Classes.Nadador import Nadador
from Classes.Pato import Pato
from Classes.Vaca import Vaca
from Classes.Voador import Voador


def fazer_som(animal):
    return animal.falar()


def fazer_movimento(animal):
    return animal.mover()


cachorro = Cachorro('Lug')
gato = Gato('Floquinho')
vaca = Vaca('Mimosa')
pato = Pato('Pato Donald')

print(fazer_som(cachorro))
print(fazer_som(gato))
print(fazer_som(vaca))
print(fazer_som(pato))

print(fazer_movimento(cachorro))
print(fazer_movimento(gato))
print(fazer_movimento(vaca))
print(fazer_movimento(pato))
