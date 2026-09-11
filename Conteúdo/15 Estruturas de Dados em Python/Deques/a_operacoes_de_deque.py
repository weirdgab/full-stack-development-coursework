from collections import deque

q = deque()           # Cria o deque

q.append('b')         # Insere no final
q.append('c')

q.appendleft('a')

print(q)              # Imprime o deque
print(q.popleft())    # Remove o inicio
print(q.pop())        # Remove o final
