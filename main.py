import customtkinter as ctk
import sqlite3
from CTkMessagebox import CTkMessagebox
from telas.login import montar_tela_login

app = ctk.CTk()

montar_tela_login(app)

app.mainloop()
