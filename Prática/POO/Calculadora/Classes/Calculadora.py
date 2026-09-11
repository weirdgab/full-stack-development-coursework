class Calculadora:
    def adicao(self, a, b):
        try:
            return int(a) + int(b)
        except TypeError:
            return 'Erro: Tipos de dados inválidos para adição.'

    def subtracao(self, a, b):
        try:
            return int(a) - int(b)
        except TypeError:
            return 'Erro: Tipos de dados inválidos para subtração.'

    def multiplicacao(self, a, b):
        try:
            return int(a) * int(b)
        except TypeError:
            return 'Erro: Tipos de dados inválidos para multiplicação.'

    def divisao(self, a, b):
        try:
            return int(a) / int(b)
        except TypeError:
            return 'Erro: Tipos de dados inválidos para divisão.'
        except ZeroDivisionError:
            return 'Erro: Não se pode dividir por zero.'
