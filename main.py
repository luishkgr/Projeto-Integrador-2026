import customtkinter as ctk
import sqlite3
from CTkMessagebox import CTkMessagebox
from telas.login import montar_tela_login
import bancodedados.banco as bd


janela_login = ctk.CTk()
bd.inicializar_db()
montar_tela_login()
janela_login.mainloop()
