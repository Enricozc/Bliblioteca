import sqlite3

conexao = sqlite3.connect("escola.db")

#Criar um obijeto "cursor" server para executar os chamados SQL
cursor = conexao.cursor()

#Criar uma tabela no banco de dados
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,        
    curso TEXT          
    )
""")
conexao.commit()
