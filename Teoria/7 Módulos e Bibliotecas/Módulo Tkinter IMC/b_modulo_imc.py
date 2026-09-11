def calcula_imc(peso, altura):
    return peso / (altura ** 2)


def classifica_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc < 25:
        return 'Peso normal'
    elif imc < 30:
        return 'Sobrepeso'
    else:
        return 'Obesidade'


if __name__ == '__main__':
    calcula_imc()
