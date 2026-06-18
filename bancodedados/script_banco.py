#Scripts para criar o banco de dados e as tabelas necessárias para o projeto.




table_usuario = ("""CREATE TABLE IF NOT EXISTS "usuario" (
 
	"id"	INTEGER NOT NULL,
 
	"nome"	VARCHAR(50) NOT NULL,
 
	"login"	VARCHAR(50) NOT NULL UNIQUE,
 
	"senha"	VARCHAR(50) NOT NULL,
 
	PRIMARY KEY("id" AUTOINCREMENT)
 
   )
              """)



table_setor = ("""CREATE TABLE IF NOT EXISTS "setor" (
 
	"id"	INTEGER NOT NULL,
 
	"nome"	VARCHAR(50) NOT NULL,
 
	"descricao" VARCHAR(50) NOT NULL,
 
	PRIMARY KEY("id" AUTOINCREMENT)
 
)
               """)
 
table_profissional =(""" CREATE TABLE IF NOT EXISTS "profissional" (
 
	"id"	INTEGER NOT NULL,
 
	"nome"	VARCHAR(50) NOT NULL,
 
	"cargo"	VARCHAR(50) NOT NULL,
 
	"status"	VARCHAR(50) NOT NULL,
	"registro_profissional"	VARCHAR(50) NOT NULL,
 
	"fone"	VARCHAR(50) NOT NULL,
 
	"email"	VARCHAR(50) NOT NULL,
 
	PRIMARY KEY("id" AUTOINCREMENT)
 
)
                     """)
 
table_plantao = ("""CREATE TABLE IF NOT EXISTS "plantao" (
 
	"id"	INTEGER NOT NULL,
 
	"setor_id"	INTEGER NOT NULL,
 
	"data"	INTEGER NOT NULL,
 
	"hora_inicio"	VARCHAR(50) NOT NULL,
	"hora_fim"	VARCHAR(50) NOT NULL,
	"quantidade_profissionais"	VARCHAR(50) NOT NULL,
 
	PRIMARY KEY("id" AUTOINCREMENT)
 
	CONSTRAINT "fk_plantao_setor" FOREIGN KEY("setor_id") REFERENCES "setor"("setor_id")
)
                 """)

table_escala =(""" CREATE TABLE IF NOT EXISTS "escala" (
 
	"id"	INTEGER NOT NULL,
 
	"profissional_id"	INTEGER NOT NULL,
 
	"plantao_id"	INTEGER NOT NULL,
 
	"status"	VARCHAR(50) NOT NULL,
 
	"data_alocacao"	VARCHAR(50) NOT NULL,
 
	"observacao"	VARCHAR(50) NOT NULL,
 
	PRIMARY KEY("id" AUTOINCREMENT)
 
	CONSTRAINT "fk_escala_profissional" FOREIGN KEY("profissional_id") REFERENCES "profissional"("profissional_id")
 
	CONSTRAINT "fk_escala_plantao" FOREIGN KEY("plantao_id") REFERENCES "plantao"("plantao_id")
)
               """)
