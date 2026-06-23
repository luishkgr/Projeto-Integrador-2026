import customtkinter as ctk
import sqlite3
from CTkMessagebox import CTkMessagebox
from telas.login import montar_tela_login
from telas.janela_principal import montar_tela_principal
import bancodedados.banco as bd
from telas.componentes import *
from utilidades.util import validar_login

app = ctk.CTk()
bd.inicializar_db()
montar_tela_login(app)
# montar_tela_login(app)

app.mainloop()
