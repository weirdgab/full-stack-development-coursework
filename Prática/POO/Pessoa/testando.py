from Classes.Pessoa import Pessoa

pessoa1 = Pessoa(nome='Gabriel', idade=19)
print(pessoa1.nome)
print(pessoa1.idade)
print(Pessoa.e_maior(pessoa1.idade))

pessoa2 = Pessoa.apartiranonasc(nome='LUG', ano=2013)
print(pessoa2.nome)
print(pessoa2.idade)
print(Pessoa.e_maior(pessoa2.idade))
