#Scripts para criar o banco de dados e as tabelas necessárias para o projeto.
table_usuario = ("""CREATE TABLE IF NOT EXISTS "usuario" (
 
	"id"	INTEGER NOT NULL,
 
	"nome"	TEXT NOT NULL,
 
	"login"	TEXT NOT NULL UNIQUE,
 
	"senha"	TEXT NOT NULL,
 
	PRIMARY KEY("id" AUTOINCREMENT)
 
   )
              """)



table_setor = ("""CREATE TABLE IF NOT EXISTS "setor" (
 
	"id"	INTEGER NOT NULL,
 
	"nome"	TEXT NOT NULL,
 
	"descricao" TEXT NOT NULL,
 
	PRIMARY KEY("id" AUTOINCREMENT)
 
)
               """)
 
table_profissional =(""" CREATE TABLE IF NOT EXISTS "profissional" (
 
	"id"	INTEGER NOT NULL,
 
	"nome"	TEXT NOT NULL,
 
	"cargo"	TEXT NOT NULL,
 
	"status" TEXT NOT NULL,
                     
	"registro_profissional"	TEXT NOT NULL UNIQUE,
 
	"fone"	TEXT NOT NULL,
 
	"email"	TEXT NOT NULL UNIQUE,
                     
    CHECK(status IN ('Ativo','Inativo', 'Afastado)),
 
	PRIMARY KEY("id" AUTOINCREMENT)
 
)
                     """)
 
table_plantao = ("""CREATE TABLE IF NOT EXISTS "plantao" (
 
	"id"	INTEGER NOT NULL,
 
	"setor_id"	INTEGER NOT NULL,
 
	"data"	DATE NOT NULL,
 
	"hora_inicio"	TIME NOT NULL,
                 
	"hora_fim"	TIME NOT NULL,
                 
	"quantidade_profissionais" INTEGER NOT NULL,
 
	PRIMARY KEY("id" AUTOINCREMENT),
 
	CONSTRAINT "fk_plantao_setor" FOREIGN KEY("setor_id") REFERENCES "setor"("id")
)
                 """)

table_escala =(""" CREATE TABLE IF NOT EXISTS "escala" (
 
	"id"	INTEGER NOT NULL,
 
	"profissional_id"	INTEGER NOT NULL,
 
	"plantao_id"	INTEGER NOT NULL,
 
	"status"	TEXT NOT NULL,
 
	"data_alocacao"	DATE NOT NULL,
 
	"observacao"	TEXT,
               
    CHECK(status IN ('Confirmada', 'Cancelada','Em andamento')),
 
	PRIMARY KEY("id" AUTOINCREMENT),
               
    UNIQUE(profissional_id, plantao_id),
 
	CONSTRAINT "fk_escala_profissional" FOREIGN KEY("profissional_id") REFERENCES "profissional"("id"),
 
	CONSTRAINT "fk_escala_plantao" FOREIGN KEY("plantao_id") REFERENCES "plantao"("id")
)
               """)
