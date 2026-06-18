import customtkinter as ctk


def mostrar_inicio(frame_conteudo):
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    frame_conteudo.grid_columnconfigure(0, weight=1)
    frame_conteudo.grid_columnconfigure(1, weight=1)
    frame_conteudo.grid_columnconfigure(2, weight=1)

    titulo = ctk.CTkLabel(
        frame_conteudo,
        text="Início",
        font=("Segoe UI Semibold", 32),
        text_color="#0B2A6F")
    titulo.grid(row=0, column=0, columnspan=3, pady=(60, 20))
    
    