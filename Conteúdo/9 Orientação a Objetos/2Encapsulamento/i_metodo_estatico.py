# Métodos estáticos podem ser chamados sem uma referência a um objeto de classe.

class MinhaClasse:
    @staticmethod  # Definindo método estático
    def metodo_estatico(x, y):
        return x + y


# Usando o método estático
resultado = MinhaClasse.metodo_estatico(x=3, y=5)
print(resultado)  # Saída: 8

# Note que você não precisa criar um instância da classe para usar o método estático.

obj = MinhaClasse()
resultado = obj.metodo_estatico(x=10, y=20)
print(resultado)  # Saída: 30
