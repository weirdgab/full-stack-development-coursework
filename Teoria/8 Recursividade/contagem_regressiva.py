print('Função recursiva de contagem regressiva a partir de 10:')

def regressiva(x):
    print(x)
    if x > 0:
        regressiva(x - 1)
    else:
        print('Acabou')
regressiva(10)

print('Função não recursiva de contagem regressiva a partir de 10:')

for y in range(10, -1, -1):
    print(y)
print('Acabou')
