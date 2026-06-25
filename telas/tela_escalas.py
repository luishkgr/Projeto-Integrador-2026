import customtkinter as ctk
from telas.componentes import *

def mostrar_escalas(frame_conteudo):

    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    frame_conteudo.grid_columnconfigure((0,1,2), weight=1)

    # ==================================================
    # TÍTULO
    # ==================================================

    titulo = ctk.CTkLabel(
        frame_conteudo,
        text="Escala do dia",
        font=("Segoe UI Semibold",32),
        text_color="#0B2A6F"
    )
    titulo.grid(row=0,column=0,columnspan=3,pady=(50,20))

    # ==================================================
    # CARD CADASTRO
    # ==================================================

    frame_horarios = ctk.CTkFrame(
        frame_conteudo,
        width=450,
        height=450,
        fg_color=COR_BRANCO,
        border_width=1,
        border_color=COR_CINZA
    )
    frame_horarios.grid(row=1,column=0,padx=15,pady=15)
    frame_horarios.grid_propagate(False)

    ctk.CTkLabel(
        frame_horarios,
        text="Cadastrar horário",
        font=("Segoe UI Semibold",18)
    ).pack(pady=20)

    frame_form = ctk.CTkFrame(
        frame_horarios,
        fg_color="transparent"
    )
    frame_form.pack(fill="both",expand=True,padx=20)

    frame_form.grid_columnconfigure((0,1),weight=1)

    ctk.CTkLabel(frame_form,text="Funcionário").grid(row=0,column=0,columnspan=2,sticky="w")
    combo = ctk.CTkComboBox(frame_form,values=[])
    combo.grid(row=1,column=0,columnspan=2,sticky="ew",pady=(0,15))

    ctk.CTkLabel(frame_form,text="Entrada").grid(row=2,column=0,sticky="w")
    entrada = ctk.CTkEntry(frame_form,placeholder_text="08:00")
    entrada.grid(row=3,column=0,padx=5,sticky="ew")

    ctk.CTkLabel(frame_form,text="Intervalo início").grid(row=2,column=1,sticky="w")
    intervalo_inicio = ctk.CTkEntry(frame_form,placeholder_text="12:00")
    intervalo_inicio.grid(row=3,column=1,padx=5,sticky="ew")

    ctk.CTkLabel(frame_form,text="Intervalo fim").grid(row=4,column=0,sticky="w",pady=(15,0))
    intervalo_fim = ctk.CTkEntry(frame_form,placeholder_text="13:00")
    intervalo_fim.grid(row=5,column=0,padx=5,sticky="ew")

    ctk.CTkLabel(frame_form,text="Saída").grid(row=4,column=1,sticky="w",pady=(15,0))
    saida = ctk.CTkEntry(frame_form,placeholder_text="17:00")
    saida.grid(row=5,column=1,padx=5,sticky="ew")

    ctk.CTkButton(
        frame_form,
        text="Salvar horário"
    ).grid(row=6,column=0,columnspan=2,pady=30)

    # ==================================================
    # CARD ESCALAS
    # ==================================================

    frame_escalas = ctk.CTkFrame(
        frame_conteudo,
        width=550,
        height=450,
        fg_color=COR_BRANCO,
        border_width=1,
        border_color=COR_CINZA
    )
    frame_escalas.grid(row=1,column=1,padx=15,pady=15)
    frame_escalas.grid_propagate(False)

    ctk.CTkLabel(
        frame_escalas,
        text="Escalas cadastradas",
        font=("Segoe UI Semibold",18)
    ).pack(pady=(15,10))

    frame_tabela = ctk.CTkFrame(
        frame_escalas,
        fg_color="transparent"
    )
    frame_tabela.pack(fill="both",expand=True,padx=10,pady=10)

    larguras = [180,140,90,90]

    cabecalho = [
        "Nome",
        "Cargo",
        "Entrada",
        "Saída"
    ]

    for coluna,titulo in enumerate(cabecalho):

        ctk.CTkLabel(
            frame_tabela,
            text=titulo,
            width=larguras[coluna],
            font=("Segoe UI Semibold",13),
            anchor="center"
        ).grid(row=0,column=coluna,pady=(0,10))

    # DADOS DE EXEMPLO
    dados = [
        ("João Silva","Enfermeiro","08:00","17:00"),
    ]

    while len(dados) < 10:
        dados.append(("","","",""))

    for linha,funcionario in enumerate(dados):

        for coluna,valor in enumerate(funcionario):

            ctk.CTkLabel(
                frame_tabela,
                text=valor,
                width=larguras[coluna],
                anchor="center",
                font=("Segoe UI",12)
            ).grid(
                row=linha+1,
                column=coluna,
                pady=5
            )