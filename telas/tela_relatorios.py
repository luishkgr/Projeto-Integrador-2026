import customtkinter as ctk


def mostrar_relatorios(frame_conteudo):
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    frame_conteudo.grid_columnconfigure(0, weight=1)
    frame_conteudo.grid_columnconfigure(1, weight=1)
    frame_conteudo.grid_columnconfigure(2, weight=1)

    titulo = ctk.CTkLabel(
        frame_conteudo,
        text="Relatorios",
        font=("Segoe UI Semibold", 32),
        text_color="#0B2A6F"
    )
    titulo.grid(row=0, column=0, columnspan=3, pady=(60, 20))

    card1 = ctk.CTkFrame(frame_conteudo, width=250, height=120)
    card1.grid(row=1, column=0, padx=20, pady=20)

    card2 = ctk.CTkFrame(frame_conteudo, width=250, height=120)
    card2.grid(row=1, column=1, padx=20, pady=20)

    card3 = ctk.CTkFrame(frame_conteudo, width=250, height=120)
    card3.grid(row=1, column=2, padx=20, pady=20)