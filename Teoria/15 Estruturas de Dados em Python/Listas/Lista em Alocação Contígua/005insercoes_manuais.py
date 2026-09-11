# Inserção direta
def insereL(k, L, n):
    L.append('')  # Aumenta um índice na lista
    L[n] = k      # Índices na lista iniciam em 0
    n += 1        # Incrementar o número de nós n


# Inserção Ordenada
def insereOrdenada(k, L, n):
    i = 0                          # Início da busca da posição
    posInsercao = -1
    while (i < n):
        if L[i] >= k:
            if L[i] == k:
                return -1          # Erro, chave já existe
            else:
                posInsercao = i    # Posição achada
                i = n + 1          # Sair do laço
        else:
            i = i + 1              # Continuar busca

        if i == n:
            posInsercao = n        # Inserção final da lista, final da busca de posição
    L.append('')                   # Aumenta um índice na lista
    i = n                          # Início do ajuste da lista
    while (i > posInsercao):
        L[i] = L[i - 1]            # Empurra cada nó para o final
    i = i - 1
    L[posInsercao] = k             # Insere novo nó
    return posInsercao             # Saída normal da função


# Testando inserções
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

insereL(12, numeros, len(numeros))
print(numeros)

insereOrdenada(5, numeros, len(numeros))
print(numeros)
