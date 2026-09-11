dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

print('Irerando sobre o dicionário:')
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')