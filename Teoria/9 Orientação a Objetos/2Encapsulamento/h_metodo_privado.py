# Método privado.
# São indicados por um (_) ou dois underscores (__) no início do nome.

class MinhaClasse:
    def __init__(self):
        self._atributo_privado = 42

    def _metodo_privado1(self):
        print('Este é um método privado.')

    def metodo_publico1(self):
        print('Este é um método público.')
        self._metodo_privado1()

    def __metodo_privado2(self):
        print('Este é um método fortemente privado.')

    def metodo_publico2(self):
        print('Este é um método público 2.')
        self.__metodo_privado2()


obj = MinhaClasse()
# Chama o método público que por sua vez chama o método privado 1.
obj.metodo_publico1()

# Saída:
# Este é um método público.
# Este é um método privado.

# Embora não seja recomendado, você ainda pode chamar diretamente o método privado.
obj._metodo_privado1()  # Funciona, mas vai contra a convenção de privacidade.
# Saída:
# Este é um método privado.

# Chama o método público que por sua vez chama o método fortemente privado.
obj.metodo_publico2()
# Saída:
# Este é um método público 2.
# Este é um método fortemente privado.

# Acessar diretamente o método fortemente privado não funciona.
# Para acessar, você teria que usar o nome "embaralhado":
obj._MinhaClasse__metodo_privado2()  # Funciona, mas não é recomendado
# Saída:
# Este é um método fortemente privado.
