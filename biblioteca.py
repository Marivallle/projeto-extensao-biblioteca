class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def __str__(self):
        return f"{self.titulo}, por {self.autor} ({self.ano}) - {'Disponível' if self.disponivel else 'Indisponível'}"


class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def adicionar_livro(self, livro):
        self.catalogo.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def listar_livros(self):
        if not self.catalogo:
            print("Nenhum livro no catálogo.")
        else:
            print("Catálogo de livros:")
            for i, livro in enumerate(self.catalogo):
                print(f"{i+1}. {livro}")

    def retirar_livro(self, titulo):
        for livro in self.catalogo:
            if livro.titulo.lower() == titulo.lower():
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"Você retirou o livro: '{livro.titulo}'")
                else:
                    print(f"O livro '{livro.titulo}' já foi retirado.")
                return
        print(f"Livro '{titulo}' não encontrado no catálogo.")

    def devolver_livro(self, titulo):
        for livro in self.catalogo:
            if livro.titulo.lower() == titulo.lower():
                if not livro.disponivel:
                    livro.disponivel = True
                    print(f"Você devolveu o livro: '{livro.titulo}'")
                else:
                    print(f"O livro '{livro.titulo}' já está disponível.")
                return
        print(f"Livro '{titulo}' não encontrado no catálogo.")


# Exemplo de uso:
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Adicionando livros à biblioteca
    livro1 = Livro("1984", "George Orwell", 1949)
    livro2 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)
    livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

    # Listar livros no catálogo
    biblioteca.listar_livros()

    # Retirar um livro
    biblioteca.retirar_livro("1984")

    # Tentar retirar o mesmo livro novamente
    biblioteca.retirar_livro("1984")

    # Devolver o livro
    biblioteca.devolver_livro("1984")

    # Tentar devolver o livro que já está disponível
    biblioteca.devolver_livro("1984")

    # Listar novamente os livros
    biblioteca.listar_livros()
