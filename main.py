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

def atualizar_disponibilidade(id_livro):
    
    cursor.execute("SELECT disponivel FROM livros WHERE id = ?", (id_livro,))
    resultado = cursor.fetchone()

    if not resultado:
        print(f"\n Nenhum livro encontrado com ID {id_livro}.")
        return

    novo_status = "Não" if resultado[0] == "Sim" else "Sim"

    cursor.execute("UPDATE livros SET disponivel = ? WHERE id = ?", (novo_status, id_livro))
    conexao.commit()
    print(f"\n🔄 Disponibilidade do livro {id_livro} atualizada para {novo_status}.")


