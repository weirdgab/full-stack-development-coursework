# Implementar uma solução em Python, através do uso de Thread, que faça:

# a. Inicie a execução de uma Thread;
# b. Coloque a thread para esperar 2 segundos
# c. Informe o início e o final da execução da thread

from threading import Thread
import time
from multiprocessing import Process


def funcao():
    for i in range(2):
        print('Executando Thread!')
        t = Thread(target=funcao, args=('Argumento 1',))
        t.start()
        p = Process(target=funcao, args=('Argumento 2',))
        p.start()
        time.sleep(2)
        print('Final da Thread!')


def main():
    print(funcao())


if __name__ == '__main__':
    main()
