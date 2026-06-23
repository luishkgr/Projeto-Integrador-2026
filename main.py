import customtkinter as ctk
import sqlite3
from CTkMessagebox import CTkMessagebox
from telas.login import montar_tela_login
from telas.janela_principal import montar_tela_principal
import bancodedados.banco as bd

app = ctk.CTk()
bd.inicializar_db()
montar_tela_principal(app)
# montar_tela_login(app)

bd.cadastro_profissional("luis", "rei", "crm12300", "4799999999", "luis@luis.com")
app.mainloop()
