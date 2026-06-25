import customtkinter as ctk
from telas.componentes import *

def mostrar_plantoes(frame_conteudo):
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    frame_conteudo.grid_columnconfigure(0, weight=1)
    frame_conteudo.grid_columnconfigure(1, weight=1)
    frame_conteudo.grid_columnconfigure(2, weight=1)

    titulo = ctk.CTkLabel(
        frame_conteudo,
        text="Plantões do dia",
        font=("Segoe UI Semibold", 32),
        text_color="#0B2A6F"
    )
    titulo.grid(row=0, column=0, columnspan=3, pady=(60, 20))

    frame_plantoes = ctk.CTkFrame(
        frame_conteudo,
        width=800,
        height=450,
        border_width=1,
        border_color=COR_CINZA,
        corner_radius=4,
        fg_color=COR_BRANCO)
    frame_plantoes.grid(row=1, column=0, columnspan=3, pady=20)
    frame_plantoes.grid_propagate(False)