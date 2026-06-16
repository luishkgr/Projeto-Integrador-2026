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
    titulo.grid(row=0, column=0, columnspan=3, pady=(60, 20))


    funcionarios =ctk.CTkFrame(
        frame_conteudo,
        border_width=1,
        corner_radius=3,
        width=800,
        height=350,
        border_color="#000000"
    )
    funcionarios.grid(row=1, column=0, columnspan=3, pady=30)

    btn_add = ctk.CTkButton(
        frame_conteudo,
        text="Adicionar Funcionário +",
        font=("Segoe UI Semibold", 14),
        text_color="#ffffff",
        width=150,
        hover_color="#2aa04d",
        height=40,
        fg_color="#30b457"
    )
    btn_add.grid(row=0, column=2, pady=(60, 20), sticky="e", padx=30)

    btn_edit = ctk.CTkButton(
        frame_conteudo,
        text="Editar",
        font=("Segoe UI Semibold", 15),
        hover_color="#343ec9",
        text_color="#ffffff",
        width=150,
        height=40,
        fg_color="#3c48eb"
    )
    btn_edit.grid(row=2, column=0, columnspan=2, padx=(200,10))

    btn_delete = ctk.CTkButton(
        frame_conteudo,
        text="Excluir",
        font=("Segoe UI Semibold", 15),
        text_color="#ffffff",
        width=150,
        height=40,
        fg_color="#f31c1c",
        hover_color="#f13535"
    )
    btn_delete.grid(row=2, column=1,columnspan=3, padx=10)