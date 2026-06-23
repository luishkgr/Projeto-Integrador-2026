import sqlite3

conexao = sqlite3.connect("bancodedados/banco.db")
cursor = conexao.cursor()

cursor.execute("""
    INSERT INTO profissional (
        nome,
        cargo,
        status,
        registro_profissional,
        fone,
        email
    )
    VALUES (?, ?, ?, ?, ?, ?)
""", (
    "Maria Oliveira Silva Silva",
    "Médica",
    "Ativo",
    "CRM 98765",
    "(47)98888-7777",
    "maria.oliveira@hospital.com"
))

conexao.commit()
conexao.close()

print("Funcionário cadastrado com sucesso!")