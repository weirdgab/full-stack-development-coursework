from threading import Thread, Lock
from multiprocessing import Process
import time

contador = 0


def funcao_a(indice):
    global contador
    for i in range(100000):
        contador += 1
    print('Término thread ', indice)


def main():
    tarefas = []
    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print('Antes de aguardar o término!', contador)

    for tarefas in tarefas:
        tarefa.join()

    print('Após aguardar o término!', contador)


if __name__ == '__main__':
    main()
