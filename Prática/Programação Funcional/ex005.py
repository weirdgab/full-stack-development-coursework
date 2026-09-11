# Implementar uma solução em Python, através do uso de Thread, que faça:

# a. Inicie a execução de duas Threads;
# b. Coloque a primeira e a segunda thread para esperar, respectivamente 3 e 2 segundos;
# C. Informe a ordem da execução das threads.

from threading import Thread
import time


def tarefa(tempo_espera, mensagem):
    print(f'\nIniciando tarefa {mensagem}')
    time.sleep(tempo_espera)
    print(f'\nConclusão da tarefa {mensagem}')


thread1 = Thread(target=tarefa, args=(3, '"Thread 1".'))
thread1.start()
print('\nAguardando pela execução da thread...')
thread1.join()
print('\nA execução foi concluída!')

thread2 = Thread(target=tarefa, args=(2, '"Thread 2".'))
thread2.start()
print('\nAguardando pela execução da thread...')
thread2.join()
print('\nA execução foi concluída!')
