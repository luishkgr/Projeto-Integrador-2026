import re

# Script direcionado para validações de dados e regras de negócio.

def aplicar_mascara_telefone(event):
    """Aplica máscara de telefone (00) 00000-0000 conforme o usuário digita"""
    entry = event.widget
    valor = entry.get().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    
    if len(valor) > 11:
        valor = valor[:11]
    
    if len(valor) <= 2:
        formatado = valor
    elif len(valor) <= 7:
        formatado = f"({valor[:2]}) {valor[2:]}"
    else:
        formatado = f"({valor[:2]}) {valor[2:7]}-{valor[7:]}"
    
    entry.delete(0, "end")
    entry.insert(0, formatado)

def validar_nome(nome):
    """Valida se o nome possui pelo menos 3 caracteres"""
    return len(nome.strip()) >= 3

def validar_email(email):
    """Valida formato de email"""
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

def validar_telefone(telefone):
    """Valida se o telefone tem 11 dígitos"""
    digitos = re.sub(r'\D', '', telefone)
    return len(digitos) == 11

def validar_registro_profissional(registro):
    """Valida se o registro profissional não está vazio"""
    return len(registro.strip()) > 0

def validar_todos_campos(nome, cargo, registro, telefone, email):
    """Valida todos os campos e retorna mensagem de erro ou True"""
    
    if not validar_nome(nome):
        return "Nome deve ter pelo menos 3 caracteres"
    
    if not cargo:
        return "Selecione um cargo"
    
    if not validar_registro_profissional(registro):
        return "Registro profissional é obrigatório"
    
    if not validar_telefone(telefone):
        return "Telefone deve conter 11 dígitos"
    
    if not validar_email(email):
        return "Email inválido"
    
    return True