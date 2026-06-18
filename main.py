import customtkinter as ctk
import sqlite3
from CTkMessagebox import CTkMessagebox
from telas.login import montar_tela_login

janela_login = ctk.CTk()
montar_tela_login()
janela_login.mainloop()
