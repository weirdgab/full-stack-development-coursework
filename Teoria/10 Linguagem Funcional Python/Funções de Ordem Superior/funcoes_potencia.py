def calcula_potencia(expoente):
    def potencia(base):
        return base ** expoente
    return potencia 

def main():
    base_expoente = input()
    base, expoente = (int(i) for i in base_expoente.split())

    potencia_de = calcula_potencia(expoente)
    res_potencia = potencia_de(base)
    print(f'{base} elevado a {expoente} = {res_potencia}')

if __name__ == "__main__":
    main()