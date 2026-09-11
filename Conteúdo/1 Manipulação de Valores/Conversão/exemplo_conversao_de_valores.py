nota1 = int(input("Digite um número inteiro: "))

nota2 = float(input("Digite um número de ponto flutuante: "))

nota3 = bool(input("Digite um valor booleano (True ou False): "))

print("\nValores convertidos:")
print(f"- Número inteiro: {nota1} (tipo: {type(nota1).__name__})")
print(f"- Número de ponto flutuante: {nota2} (tipo: {type(nota2).__name__})")
print(f"- Valor booleano: {nota3} (tipo: {type(nota3).__name__})")