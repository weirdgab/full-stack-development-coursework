# Implementar uma solução em Python, através do uso de Thread, que faça:

# a. Inicie a execução de duas Threads;
# b. A primeira Thread deve calcular o quadrado de um número;
# c. A segunda Thread deve calcular o quadrado de um número;
# d. Coloque a primeira e a segunda threads para esperar, respectivamente, 3 e 2 segundos;
# e. Informe a ordem da execução das threads.

from threading import Thread
from time import sleep


def quadrado(tempo_espera, n):
    sleep(tempo_espera)
    print(f'O quadrado de {n} é {n ** 2}.')


def cubo(tempo_espera, n):
    sleep(tempo_espera)
    print(f'O cubo de {n} é {n ** 3}')


t1 = Thread(target=quadrado, args=(
    3, int(input('Digite um número para verificar seu valor ao quadrado (primeira Thread): '))))
t2 = Thread(target=cubo, args=(
    2, int(input('Digite um número para verificar seu valor ao cubo (segunda Thread): '))))
t1.start()
print('Thread 1 iniciada.')
t1.join()
print('Thread 1 concluída.')
t2.start()
print('Thread 2 iniciada.')
t2.join()
print('Thread 2 concluída.')
