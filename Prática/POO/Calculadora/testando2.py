class Calculadora:
    def adicao(self, a, b):
        try:
            return int(a) + int(b)
        except TypeError:
            return 'Erro: tipo de dados não suportado'

    def subtracao(self, a, b):
        try:
            return int(a) - int(b)
        except TypeError:
            return 'Erro: tipo de dados não suportado'

    def multiplicacao(self, a, b):
        try:
            return int(a) * int(b)
        except TypeError:
            return 'Erro: tipo de dados não suportado'

    def divisao(self, a, b):
        try:
            return int(a) / int(b)
        except TypeError:
            return 'Erro: tipo de dados não suportado'
        except ZeroDivisionError:
            return 'Erro: valor não pode ser zero.'


calculadora = Calculadora()

print(calculadora.adicao(2, 2))
print(calculadora.subtracao(2, 2))
print(calculadora.multiplicacao(2, 2))
print(calculadora.divisao(2, 2))
