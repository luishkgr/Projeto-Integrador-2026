import customtkinter as ctk
import sqlite3
from CTkMessagebox import CTkMessagebox
from telas.login import montar_tela_login
from telas.janela_principal import montar_tela_principal
import bancodedados.banco as bd
from telas.componentes import *
from utilidades.util import validar_login

def login_valido():
    montar_tela_principal(app)

app = ctk.CTk()
bd.inicializar_db()
montar_tela_login(app, login_valido)

app.mainloop()
