valores = input()

valores = [int(i) for i in valores.split()]


def altera_lista(lista):
    lista[2] = lista[2] + 10


def main():
    print('Nova Lista', altera_lista(valores))
    print('Nova Lista', altera_lista(valores))


if __name__ == '__main__':
    main()
