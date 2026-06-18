import customtkinter as ctk
import sqlite3
from CTkMessagebox import CTkMessagebox
from telas.login import montar_tela_login
import bancodedados.banco as bd

<<<<<<< HEAD
app = ctk.CTk()
bd.inicializar_db()
montar_tela_login(app)



=======

app = ctk.CTk()
bd.inicializar_db()
montar_tela_login(app)
>>>>>>> 71ad57c10ca8a9098f9fabd55b5e36bb41e0fa0e
app.mainloop()
