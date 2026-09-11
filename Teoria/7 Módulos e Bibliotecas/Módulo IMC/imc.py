print("Módulo IMC importado")

def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

if __name__ == '__main__':
    print(calcula_imc(70, 1.8))
    