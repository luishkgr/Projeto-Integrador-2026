import customtkinter as ctk
from telas.componentes import *

def mostrar_escalas(frame_conteudo):
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    frame_conteudo.grid_columnconfigure((0, 1, 2), weight=1)

    titulo = ctk.CTkLabel(
        frame_conteudo,
        text="Escala do dia",
        font=("Segoe UI Semibold", 32),
        text_color="#0B2A6F"
    )
    titulo.grid(row=0, column=0, columnspan=3, pady=(60, 20))

#region Escalas 

    frame_escalas = ctk.CTkFrame(
        frame_conteudo,
        width=450,
        height=450,
        border_width=1,
        border_color=COR_CINZA,
        corner_radius=4,
        fg_color=COR_BRANCO
    )
    frame_escalas.grid(row=1, column=1, pady=20)
    frame_escalas.grid_propagate(False)
    frame_escalas.grid_columnconfigure(0, weight=1)

#endregion

#region escalas dos funcionarios

    label_escalas = ctk.CTkLabel(
        frame_escalas,
        text="Escala dos funcionarios",
        font=("Segoe UI Semibold", 18)
    )
    label_escalas.grid(row=0, column=0, pady=20)

    

#endregion

#region Cadastro de Horários
    frame_horarios = ctk.CTkFrame(
        frame_conteudo,
        width=450,
        height=450,
        border_width=1,
        border_color=COR_CINZA,
        corner_radius=4,
        fg_color=COR_BRANCO
    )
    frame_horarios.grid(row=1, column=0, padx=10, pady=10)
    frame_horarios.grid_propagate(False)
    frame_horarios.grid_columnconfigure(0, weight=1)

    ctk.CTkLabel(
        frame_horarios,
        text="Cadastrar horário do funcionario",
        font=("Segoe UI Semibold", 18)
    ).grid(row=0, column=0, pady=20)

    frame_cad_hora = ctk.CTkFrame(
        frame_horarios,
        width=380,
        height=320,
        fg_color=COR_BRANCO
    )
    frame_cad_hora.grid(row=1, column=0)
    frame_cad_hora.grid_propagate(False)

    
    frame_cad_hora.grid_columnconfigure(0, weight=1)
    frame_cad_hora.grid_columnconfigure(1, weight=1)

    #endregion

    #region selecionar horas
    
    ctk.CTkLabel(
        frame_cad_hora,
        text="Funcionário"
    ).grid(row=0, column=0, sticky="w", padx=20, pady=(20,5))

    combo_funcionario = ctk.CTkComboBox(
        frame_cad_hora,
        values=[]
    )
    combo_funcionario.grid(row=1, column=0, columnspan=2, padx=20, sticky="ew")

    
    ctk.CTkLabel(
        frame_cad_hora,
        text="Entrada"
    ).grid(row=2, column=0, sticky="w", padx=20, pady=(20,5))

    entrada = ctk.CTkEntry(
        frame_cad_hora,
        placeholder_text="08:00"
    )
    entrada.grid(row=3, column=0, padx=20, sticky="ew")

    
    ctk.CTkLabel(
        frame_cad_hora,
        text="Início intervalo"
    ).grid(row=2, column=1, sticky="w", padx=20, pady=(20,5))

    saida = ctk.CTkEntry(
        frame_cad_hora,
        placeholder_text="17:00"
    )
    saida.grid(row=3, column=1, padx=20, sticky="ew")

    ctk.CTkLabel(
        frame_cad_hora,
        text="Fim intervalo"
    ).grid(row=4, column=0, sticky="w", padx=20, pady=(20,5))

    entrada = ctk.CTkEntry(
        frame_cad_hora,
        placeholder_text="08:00"
    )
    entrada.grid(row=5, column=0, padx=20, sticky="ew")

    ctk.CTkLabel(
        frame_cad_hora,
        text="Saída"
    ).grid(row=4, column=1, sticky="w", padx=20, pady=(20,5))

    saida = ctk.CTkEntry(
        frame_cad_hora,
        placeholder_text="17:00"
    )
    saida.grid(row=5, column=1, padx=20, sticky="ew")

#endregion

    #region btn salvar

    ctk.CTkButton(
        frame_cad_hora,
        text="Salvar horário"
    ).grid(row=6, column=0, columnspan=2, pady=30)

#endregion