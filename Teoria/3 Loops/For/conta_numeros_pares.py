def conta_numeros_pares(n):
    p = 0
    for num in range(n+1):
        if num % 2 == 0:
            p += 1
    return p


teste = conta_numeros_pares(int(input('Digite um número: ')))

print(teste)
