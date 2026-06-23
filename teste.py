import sqlite3

conexao = sqlite3.connect("bancodedados/banco.db")
cursor = conexao.cursor()

cursor.execute("""
INSERT INTO usuario (nome, login, senha)
VALUES (?, ?, ?)
""", (
    "Administrador",
    "admin",
    "123"
))

conexao.commit()
conexao.close()

print("Usuário cadastrado com sucesso!")