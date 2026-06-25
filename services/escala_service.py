from bancodedados import banco as bd

def existe_conflito_por_profissional(profissional_id, plantao_id, escala_id=None):
    plantao = bd.obter_plantao_por_id(plantao_id)
    if plantao is None:
        raise ValueError(f"Plantão não encontrado: {plantao_id}")

    _, setor_novo, data_novo, hora_inicio_novo, hora_fim_novo = plantao
    escalas = bd.listar_escalas_por_profissional_e_data(profissional_id, data_novo)

    for escala_existente_id, setor_existente, hora_inicio_existente, hora_fim_existente in escalas:
        if escala_id is not None and escala_existente_id == escala_id:
            continue
        if hora_inicio_existente < hora_fim_novo and hora_fim_existente > hora_inicio_novo:
            if setor_existente != setor_novo:
                return True

    return False

def validar_conflito_escala(profissional_id, plantao_id, escala_id=None):
    if existe_conflito_por_profissional(profissional_id, plantao_id, escala_id):
        raise ValueError(
            "Conflito de horário: o profissional já está escalado em outro setor no mesmo horário."
        )

def cadastrar_escala(profissional_id, plantao_id, status, data_alocacao, observacao=None):
    validar_conflito_escala(profissional_id, plantao_id)
    return bd.inserir_escala(profissional_id, plantao_id, status, data_alocacao, observacao)

def atualizar_escala(escala_id, profissional_id, plantao_id, status, data_alocacao, observacao=None):
    validar_conflito_escala(profissional_id, plantao_id, escala_id)
    bd.atualizar_escala(escala_id, profissional_id, plantao_id, status, data_alocacao, observacao)

def consultar_escala(escala_id):
    return bd.consultar_escala(escala_id)

def listar_escalas():
    return bd.listar_escalas()