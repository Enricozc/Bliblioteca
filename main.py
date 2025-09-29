import sqlite3
import streamlit as st

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
    print(f"\n Disponibilidade do livro {id_livro} atualizada para {novo_status}.")

def remover_livro(id_livro):
    cursor.execute("SELECT * FROM livros WHERE id = ?", (id_livro,))
    if not cursor.fetchone():
        print(f"\n Nenhum livro encontrado com ID {id_livro}.")
        return

    cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
    conexao.commit()
    print(f"\n Livro com ID {id_livro} removido com sucesso.")


st.title("📚 Biblioteca com Streamlit")

menu = st.sidebar.radio("Menu", ["Cadastrar Livro", "Listar Livros", "Atualizar Disponibilidade", "Remover Livro"])

if menu == "Cadastrar Livro":
    st.subheader("Cadastrar Novo Livro")
    titulo = st.text_input("Título")
    autor = st.text_input("Autor")
    ano = st.number_input("Ano", min_value=0, max_value=2100, step=1)

    if st.button("Cadastrar"):
        if titulo and autor:
            cadastrar_livro(titulo, autor, ano)
            st.success(f"Livro '{titulo}' cadastrado com sucesso!")
        else:
            st.error("Preencha todos os campos obrigatórios!")

