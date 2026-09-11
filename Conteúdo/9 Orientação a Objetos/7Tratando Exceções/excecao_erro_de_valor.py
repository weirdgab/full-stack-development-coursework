while True:
    try:
        nr = int(input('Digite um número: '))
        s = nr * 3
        print(s)
        q = 12 / s
        print(q)
        # Final do loop
        break
    # Tratamento do erro
    except ValueError:
        print('Entre com um número válido: ')