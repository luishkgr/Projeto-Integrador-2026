import customtkinter as ctk
import sqlite3
from CTkMessagebox import CTkMessagebox
from telas.login import montar_tela_login
import bancodedados.banco as bd
from telas.componentes import *

app = ctk.CTk()
bd.inicializar_db()
montar_tela_login(app)



app.mainloop()
