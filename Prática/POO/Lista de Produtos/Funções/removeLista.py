def removeLista(k, L, n):
    i = 0
    posRemocao = -1
    while (i < n):
        if L[i] == k:
            posRemocao = i
            i = n + 1
        else:
            i = i + 1
    if i == n:
        return -1
    i = posRemocao
    while (i < n - 1):
        L[i] = L[i + 1]
        i = i + 1
    L.pop(n - 1)
    return posRemocao
