import os
import sqlite3
import bancodedados.script_banco as script_banco

DB_NAME = os.path.join(os.path.dirname(__file__), "banco.db")

# region Conexão e inicialização
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
    conn.close()
# endregion

# region Usuário
def validar_usuario(login, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nome, login, senha FROM usuario WHERE login = ?",
        (login.strip(),)
    )
    resultado = cursor.fetchone()
    print("validar_usuario:", repr(login.strip()), "resultado:", resultado)
    conn.close()
    return bool(resultado and resultado[3] == senha.strip())

def cadastro_usuario(nome, login, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuario (nome, login, senha) VALUES (?, ?, ?)",
        (nome, login, senha)
    )
    conn.commit()
    usuario_id = cursor.lastrowid
    conn.close()
    return usuario_id

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, login, senha FROM usuario ORDER BY nome")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

def consultar_usuario(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nome, login, senha FROM usuario WHERE id = ?",
        (usuario_id,)
    )
    usuario = cursor.fetchone()
    conn.close()
    return usuario

def atualizar_usuario(usuario_id, nome, login, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE usuario SET nome = ?, login = ?, senha = ? WHERE id = ?",
        (nome, login, senha, usuario_id)
    )
    conn.commit()
    conn.close()

def excluir_usuario(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuario WHERE id = ?", (usuario_id,))
    conn.commit()
    conn.close()
# endregion

# region Setor
def cadastro_setor(nome, descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO setor (nome, descricao) VALUES (?, ?)",
        (nome, descricao)
    )
    conn.commit()
    setor_id = cursor.lastrowid
    conn.close()
    return setor_id

def listar_setores():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, descricao FROM setor ORDER BY nome")
    setores = cursor.fetchall()
    conn.close()
    return setores

def consultar_setor(setor_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nome, descricao FROM setor WHERE id = ?",
        (setor_id,)
    )
    setor = cursor.fetchone()
    conn.close()
    return setor

def atualizar_setor(setor_id, nome, descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE setor SET nome = ?, descricao = ? WHERE id = ?",
        (nome, descricao, setor_id)
    )
    conn.commit()
    conn.close()

def excluir_setor(setor_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM setor WHERE id = ?", (setor_id,))
    conn.commit()
    conn.close()
# endregion

# region Profissional
def cadastro_profissional(nome, cargo, registro_profissional, fone, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO profissional (nome, cargo, status, registro_profissional, fone, email) VALUES (?, ?, 'Ativo', ?, ?, ?)",
        (nome, cargo, registro_profissional, fone, email)
    )
    conn.commit()
    profissional_id = cursor.lastrowid
    conn.close()
    return profissional_id

def listar_profissionais():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nome, cargo, status, registro_profissional, fone, email FROM profissional ORDER BY nome"
    )
    profissionais = cursor.fetchall()
    conn.close()
    return profissionais

def consultar_profissional(profissional_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nome, cargo, status, registro_profissional, fone, email FROM profissional WHERE id = ?",
        (profissional_id,)
    )
    profissional = cursor.fetchone()
    conn.close()
    return profissional

def atualizar_profissional(profissional_id, nome, cargo, status, registro_profissional, fone, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE profissional SET nome = ?, cargo = ?, status = ?, registro_profissional = ?, fone = ?, email = ? WHERE id = ?",
        (nome, cargo, status, registro_profissional, fone, email, profissional_id)
    )
    conn.commit()
    conn.close()

def excluir_profissional(profissional_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM profissional WHERE id = ?", (profissional_id,))
    conn.commit()
    conn.close()
# endregion

# region Plantão
def cadastro_plantao(setor_id, data, hora_inicio, hora_fim, quantidade_profissionais):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO plantao (setor_id, data, hora_inicio, hora_fim, quantidade_profissionais) VALUES (?, ?, ?, ?, ?)",
        (setor_id, data, hora_inicio, hora_fim, quantidade_profissionais)
    )
    conn.commit()
    plantao_id = cursor.lastrowid
    conn.close()
    return plantao_id

def listar_plantoes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, setor_id, data, hora_inicio, hora_fim, quantidade_profissionais FROM plantao ORDER BY data, hora_inicio"
    )
    plantoes = cursor.fetchall()
    conn.close()
    return plantoes

def consultar_plantao(plantao_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, setor_id, data, hora_inicio, hora_fim, quantidade_profissionais FROM plantao WHERE id = ?",
        (plantao_id,)
    )
    plantao = cursor.fetchone()
    conn.close()
    return plantao

def atualizar_plantao(plantao_id, setor_id, data, hora_inicio, hora_fim, quantidade_profissionais):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE plantao SET setor_id = ?, data = ?, hora_inicio = ?, hora_fim = ?, quantidade_profissionais = ? WHERE id = ?",
        (setor_id, data, hora_inicio, hora_fim, quantidade_profissionais, plantao_id)
    )
    conn.commit()
    conn.close()

def excluir_plantao(plantao_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM plantao WHERE id = ?", (plantao_id,))
    conn.commit()
    conn.close()
# endregion

# region Escala
def cadastro_escala(profissional_id, plantao_id, status, data_alocacao, observacao):
    return inserir_escala(profissional_id, plantao_id, status, data_alocacao, observacao)

def inserir_escala(profissional_id, plantao_id, status, data_alocacao, observacao=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO escala (profissional_id, plantao_id, status, data_alocacao, observacao) VALUES (?, ?, ?, ?, ?)",
        (profissional_id, plantao_id, status, data_alocacao, observacao)
    )
    conn.commit()
    last_id = cursor.lastrowid
    conn.close()
    return last_id

def consultar_escala(escala_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, profissional_id, plantao_id, status, data_alocacao, observacao FROM escala WHERE id = ?",
        (escala_id,)
    )
    escala = cursor.fetchone()
    conn.close()
    return escala

def listar_escalas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT e.id, e.profissional_id, e.plantao_id, e.status, e.data_alocacao, e.observacao,
               p.nome AS profissional_nome, pl.setor_id, pl.data, pl.hora_inicio, pl.hora_fim
        FROM escala e
        INNER JOIN profissional p ON e.profissional_id = p.id
        INNER JOIN plantao pl ON e.plantao_id = pl.id
        ORDER BY pl.data, pl.hora_inicio
        """
    )
    escalas = cursor.fetchall()
    conn.close()
    return escalas

def excluir_escala(escala_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM escala WHERE id = ?", (escala_id,))
    conn.commit()
    conn.close()
# endregion

# region Consultas auxiliares
def obter_plantao_por_id(plantao_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, setor_id, data, hora_inicio, hora_fim FROM plantao WHERE id = ?",
        (plantao_id,)
    )
    plantao = cursor.fetchone()
    conn.close()
    return plantao

def obter_escala_por_id(escala_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, profissional_id, plantao_id, status, data_alocacao, observacao FROM escala WHERE id = ?",
        (escala_id,)
    )
    escala = cursor.fetchone()
    conn.close()
    return escala

def listar_escalas_por_profissional_e_data(profissional_id, data):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT e.id, pl.setor_id, pl.hora_inicio, pl.hora_fim
        FROM escala e
        INNER JOIN plantao pl ON e.plantao_id = pl.id
        WHERE e.profissional_id = ? AND pl.data = ?
        """,
        (profissional_id, data)
    )
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def atualizar_escala(escala_id, profissional_id, plantao_id, status, data_alocacao, observacao=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE escala
        SET profissional_id = ?, plantao_id = ?, status = ?, data_alocacao = ?, observacao = ?
        WHERE id = ?
        """,
        (profissional_id, plantao_id, status, data_alocacao, observacao, escala_id)
    )
    conn.commit()
    conn.close()
# endregion

