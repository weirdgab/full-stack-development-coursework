# Implementar uma solução através de programação funcional para arrendondar os valores da lista de números na mesma ordem da lista de precisão.
import math

lista_numeros = [9.56783, 7.57568, 3.00914, 6.2321]

lista_precisao = [2, 2, 3, 3]

lista_numeros0 = math.floor(lista_numeros[0])
lista_numeros1 = math.floor(lista_numeros[1])
lista_numeros2 = math.floor(lista_numeros[2])
lista_numeros3 = math.floor(lista_numeros[3])

listaModificada = [lista_numeros2, lista_numeros3,
                   lista_numeros1, lista_numeros0]

print(listaModificada)
