# Procedimento para trocar elemento com o próximo - def trocar()
def trocar(seq, i):
    aux = seq[i]
    seq[i] = seq[i+1]
    seq[i+1] = aux

# Inicialização da sequencia de teste - seq=[]
seq = [1,15,22,6,7,19,8,3,5,20]

# Variável de controle do laço - troca
troca = 1

# Laço das múltiplas passagens - while troca:
while troca:
    troca = 0
    i = 0
    # Laço interno de uma passagem - for i in range...
    for i in range(len(seq)-1):
        if seq[i]>seq[i+1]:
            trocar(seq,i)
            troca = 1

# Impressão da sequência ordenada - print(seq)
print(seq )