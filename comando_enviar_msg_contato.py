import comando_enviar_msg_contato_IMP

def processa(ses, msg):
    """Esta função é chamada quando o usuário aperta o botão "Enviar" no formulario
    de contato (vide {html_form_contato}).

    O parâmetro {args} é um dicionário que contém os valores inseridos nos campos do 
    formulario ("nome", "e-mail", "telefone", "assunto")

    O resultado deve ser uma página com uma mensagem padrao de resposta"""
    return comando_enviar_msg_contato_IMP.processa(ses, msg)