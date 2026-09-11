texto = "Olá, Mundo!"
print(texto)

# Formatação de stings
idade = 30
cidade = "São Paulo"
frase_formatada = f'Meu nome é {nome}, tenho {idade} anos e moro em {cidade}.'
print(f'Frase formatada: {frase_formatada}')

# Outro método de formatação
frase_formatada_2 = "Meu nome é {}, tenho {} anos e moro em {}.".fromat(nome, idade, cidade)
print(f'Outra frase formatada: {frase_formatada_2}')