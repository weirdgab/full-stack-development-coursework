def conta_numeros_pares(n):
    if n == 0:
        return 1  # 0 é par
    elif n % 2 == 0:
        return 1 + conta_numeros_pares(n-1)
    else:
        return conta_numeros_pares(n-1)


teste = conta_numeros_pares(int(input('Digite um número: ')))

print(conta_numeros_pares(teste))
