import sqlite3
import bancodedados.script_banco as script_banco

DB_NAME = "./bancodedados/banco.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def inicializar_db():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(script_banco.table_usuario)
    cursor.execute(script_banco.table_setor)
    cursor.execute(script_banco.table_profissional)
    cursor.execute(script_banco.table_plantao)
    cursor.execute(script_banco.table_escala)

    conn.commit()
    
# CRUD

# CREATE - INSERT
# READ - SELECT
# UPDATE - UPDATE
# DELETE - DELETE

def cadastro_profissional(nome, cargo, registro_profissional, fone, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """
                    INSERT INTO profissional (nome, cargo, status, registro_profissional, fone, email) VALUES (?, ?, "ativo", ?,?,?)
                   """, (nome, cargo, registro_profissional, fone, email,))
    conn.commit()
    conn.close()



