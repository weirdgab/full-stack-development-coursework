from b_funções_caso_contiguo import pop, push

maxPilha = 10
pilha = [None] * maxPilha
topoPilha = None

print(pilha)
for i in range(10):
    push(i)
    print(pilha)
print(push(11))

for i in range(10):
    print(pop())
print(pop())
