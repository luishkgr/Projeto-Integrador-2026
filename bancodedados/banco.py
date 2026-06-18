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
    
