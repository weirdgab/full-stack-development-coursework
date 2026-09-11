valores = input()

valores = [int(i) for i in valores.split()]


def altera_lista(lista):
    nova_lista = list(lista)
    nova_lista[2] = nova_lista[2] + 10
    return lista


def main():
    print('Nova Lista', altera_lista(valores))
    print('Nova Lista', altera_lista(valores))

    if __name__ == '__name__':
        main()
