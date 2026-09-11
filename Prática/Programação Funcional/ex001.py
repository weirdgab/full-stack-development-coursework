# Implementar uma solução através de programação funcional para imprimir apenas os números pares.
lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

lista_par = filter(lambda item: item % 2 == 0, lista)


def main():
    print(list(lista_par))


if __name__ == '__main__':
    main()
