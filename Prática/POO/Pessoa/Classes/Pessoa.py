from datetime import date


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Um método de classe para criar um objeto pessoa a partir do ano de nascimento
    @classmethod
    def apartiranonasc(cls, nome, ano):
        return cls(nome, date.today().year - ano)

    # Método estático para verificar se é maior de idade
    @staticmethod
    def e_maior(idade):
        return idade >= 18
