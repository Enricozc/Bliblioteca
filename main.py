import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT CHECK(disponivel IN ('Sim', 'Não')) NOT NULL
)
""")

conexao.commit()

def cadastrar_livro(titulo, autor, ano):
    cursor.execute("""
        INSERT INTO livros (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, 'Sim')
    """, (titulo, autor, ano))
    conexao.commit()
    print(f" Livro '{titulo}' cadastrado com sucesso!")


def listar_livros():

    cursor.execute("SELECT id, titulo, autor, ano, disponivel FROM livros")
    livros = cursor.fetchall()

    if not livros:
        print("Nenhum livro cadastrado ainda.")
        return

    print("\n Lista de Livros Cadastrados:")
    print("-" * 60)
    for livro in livros:
        print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Ano: {livro[3]} | Disponível: {livro[4]}")
    print("-" * 60)

if __name__ == "__main__":
    cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899)
    cadastrar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

    listar_livros()
