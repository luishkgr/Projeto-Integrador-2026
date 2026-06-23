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

#cadastro
 
def cadastro_usuario(nome, login, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                    INSERT INTO usuario (nome, login, senha) VALUES (?, ?, ?)

                   """, (nome, login, senha,))

    conn.commit()
    conn.close()
 
def cadastro_setor(nome, descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                    INSERT INTO setor (nome, descricao) VALUES (?, ?)

                   """, (nome, descricao,))

    conn.commit()
    conn.close()
 
def cadastro_profissional(nome, cargo, registro_profissional, fone, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                    INSERT INTO profissional (nome, cargo, status, registro_profissional, fone, email) VALUES (?, ?, "Ativo", ?,?,?)

                   """, (nome, cargo, registro_profissional, fone, email,))

    conn.commit()
    conn.close()
 
def cadastro_plantao(setor_id, data, hora_inicio, hora_fim, quantidade_profissionais):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute( """

                    INSERT INTO plantao (setor_id, data, hora_inicio, hora_fim, quantidade_profissionais) VALUES (?, ?, ?, ?, ?)

                   """, (setor_id, data, hora_inicio, hora_fim, quantidade_profissionais,))

    conn.commit()
    conn.close()
 
def cadastro_escala(profissional_id, plantao_id, status, data_alocacao, observacao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                    INSERT INTO escala (profissional_id, plantao_id, status, data_alocacao, observacao) VALUES (?, ?, ?, ?, ?)

                   """, (profissional_id, plantao_id, status, data_alocacao, observacao,))

    conn.commit()
    conn.close()
 
#====================================================================================================================================
 
#consultar
 
def consultar_usuario(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                   SELECT * FROM usuario WHERE id = ?

                   """, (usuario_id,))

    conn.commit()
    conn.close()
 
def consultar_setor(setor_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                    SELECT * FROM setor WHERE id = ?

                   """, (setor_id,))

    conn.commit()
    conn.close()
 
def consultar_profissional(profissional_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                    SELECT * FROM profissional WHERE id = ?

                   """, (profissional_id,))

    conn.commit()
    conn.close()
 
def consultar_plantao(plantao_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                    SELECT * FROM plantao WHERE id = ?

                   """, (plantao_id,))

    conn.commit()
    conn.close()

def consultar_escala(escala_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                    SELECT * FROM escala WHERE id = ?

                   """, (escala_id,))

    conn.commit()
    conn.close()
 
#====================================================================================================================================
 
#atualizar
 
def atualizar_usuario(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                   UPDATE usuario SET (nome, login, senha) = (?,?,?) WHERE id = ?

                   """, (usuario_id,))

    conn.commit()
    conn.close()
 
def atualizar_setor(setor_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                    UPDATE setor SET (nome, descricao) = (?,?) WHERE id = ?

                   """, (setor_id,))

    conn.commit()
    conn.close()
 
def atualizar_profissional(profissional_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                     UPDATE profissional SET (nome, cargo, status, registro_profissional, fone, email) = (?,?,?,?,?,?) WHERE id = ?

                   """, (profissional_id,))

    conn.commit()
    conn.close()
 
def atualizar_plantao(plantao_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                    UPDATE plantao SET (data, hora_inicio, hora_fim, quantidade_profissionais) = (?,?,?,?) WHERE id = ?

                   """, (plantao_id,))

    conn.commit()
    conn.close()
 
def atualizar_escala(escala_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                     UPDATE escala SET (plantao_id, status, data_alocacao, observacao) = (?,?,?,?,?) WHERE id = ?

                   """, (escala_id,))

    conn.commit()
    conn.close()
 
#====================================================================================================================================
 
#deletar
 
def delete_usuario(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                   DELETE FROM usuario WHERE id = ?

                   """, (usuario_id,))

    conn.commit()
    conn.close()
 
def delete_setor(setor_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                   DELETE FROM setor WHERE id = ?

                   """, (setor_id,))

    conn.commit()
    conn.close()
 
def delete_profissional(profissional_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                     DELETE FROM profissional WHERE id = ?

                   """, (profissional_id,))

    conn.commit()
    conn.close()
 
def delete_plantao(plantao_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                    DELETE FROM plantao WHERE id = ?

                   """, (plantao_id,))

    conn.commit()
    conn.close()
 
def delete_escala(escala_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute( """

                     DELETE FROM escala WHERE id = ?

                   """, (escala_id,))

    conn.commit()
    conn.close()

 