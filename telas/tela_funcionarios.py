import customtkinter as ctk


def mostrar_funcionarios(frame_conteudo):
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    frame_conteudo.grid_columnconfigure(0, weight=1)
    frame_conteudo.grid_columnconfigure(1, weight=1)
    frame_conteudo.grid_columnconfigure(2, weight=1)

    titulo = ctk.CTkLabel(
        frame_conteudo,
        text="Funcionarios",
        font=("Segoe UI Semibold", 32),
        text_color="#0B2A6F"
    )
    titulo.grid(row=0, column=0, columnspan=3, pady=(60, 40))

    btn_add = ctk.CTkButton(
        frame_conteudo,
        text="Adicionar",
        font=("Segoe UI Semibold", 15),
        text_color="#ffffff",
        width=150,
        hover_color="#2aa04d",
        height=50,
        fg_color="#30b457"
    )
    btn_add.grid(row=1, column=0)

    btn_edit = ctk.CTkButton(
        frame_conteudo,
        text="Editar",
        font=("Segoe UI Semibold", 15),
        text_color="#343ec9",
        width=150,
        height=50,
        fg_color="#3c48eb"
    )
    btn_edit.grid(row-1, column=1, columnspan=2)