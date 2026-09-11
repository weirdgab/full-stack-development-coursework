# Testando as classes

# Criando alguns livros
from Classes.Biblioteca import Biblioteca
from Classes.Livro import Livro

livro1 = Livro(titulo='O Senhor dos Anéis',
               autor='J.R.R Tolkien', isbn='1234567890')
livro2 = Livro(titulo='1984', autor='George Orwell', isbn='0987654321')
livro3 = Livro(titulo='O Apanhador no Campo de Centeio',
               autor='J.D Salinger', isbn='1122334455')

# Criando uma biblioteca
biblioteca = Biblioteca('Biblioteca Central')

# Adicionando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Listando todos os livros na biblioteca
biblioteca.listar_livros()

# Removendo um livro na biblioteca
biblioteca.remover_livro('0987654321')

# Listando todos os livros na biblioteca após a remoção
biblioteca.listar_livros()
