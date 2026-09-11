def calcula_imc(peso, altura):
    return peso / (altura ** 2)

def main():
    indice = calcula_imc(70, 1.80)
    print(f'IMC: {indice:.2f}')

    if indice < 18.5:
        print("Abaixo do peso")
    elif indice < 25:
        print("Peso normal")
    elif indice < 30:
        print("Sobrepeso")
    else:
        print("Obesidade")

if __name__ == "__main__":
    main()