saida = ''


def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    if x == 0:
        return 'Não foi possível completar a divisão.'
    elif y == 0:
        return 'Não foi possível completar a divisão.'
    else:
        return x / y


def calculadora(x, y, operacao):
    if operacao == 'Adição':
        resultado = adicao(x, y)
        return resultado
    elif operacao == 'Subtração':
        resultado = subtracao(x, y)
        return resultado
    elif operacao == 'Multiplicação':
        resultado = multiplicacao(x, y)
        return resultado
    elif operacao == 'Divisão':
        resultado = divisao(x, y)
        return resultado
    else:
        return 'Operação inexistente, verifique a ortografia!'


sair = False

while not sair:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    operacao = input(
        'Adição, Subtração, Multiplicação, Divisão.\nDigite uma das operações escritas acima: ')
    resultado = calculadora(n1, n2, operacao)
    print('O resultado desta operação é: ', resultado)
    saida = input('Deseja continuar? Digite S/N: ')

    if saida.lower() == 'n':
        sair = True
    elif saida.lower() == 's':
        print('Programa reiniciado!\n')
    else:
        while True:
            print('Valor digitado não reconhecido, tente novamente.')
            saida = input('Deseja continuar? Digite S/N: ')
            if saida.lower() == 'n':
                sair = True
                break
            elif saida.lower() == 's':
                break
print('Programa encerrado.')
