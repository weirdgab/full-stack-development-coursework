texto = input("Digite a palavra para ser usada: ")
letras_para_contar = input("Digite a letra para ser contada: ")
contador = 0

for letra in texto:
    if letra == letras_para_contar:
        contador += 1

if contador == 1:
    print(f"A letra {letras_para_contar} aparece {contador} vez na palavra {texto}")
else:
    print(f"A letra {letras_para_contar} aparece {contador} vezes na palavra {texto}")