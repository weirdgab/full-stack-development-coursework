class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'Livro "{livro.titulo}" adicionado à biblioteca "{self.nome}".')

    def remover_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                print(
                    f'Livro "{livro.titulo}" removido da biblioteca "{self.nome}".')
                return
        print(
            f'Livro com ISBN {isbn} não encontrado na biblioteca "{self.nome}".')

    def listar_livros(self):
        if not self.livros:
            print(f'A biblioteca "{self.nome}" não tem livros.')
        else:
            print(f'Livros na biblioteca "{self.nome}":')
            for livro in self.livros:
                print(f'- {livro.titulo} port {livro.autor} (ISBN: {livro.isbn})')

    def buscar_livro_por_titulo(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                print(
                    f'Livro encontrado: {livro.titulo} por {livro.autor} (ISBN: {livro.isbn})')
                return livro
        print(
            f'Livro com o título "{titulo}" não encontrado na biblioteca "{self.nome}".')
        return None
