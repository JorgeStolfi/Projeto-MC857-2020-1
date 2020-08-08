# Implementação do módulo {comando_fechar_sessao}.

import html_pag_sessao
import html_pag_mensagem_de_erro
import html_pag_principal
import sessao

def processa(ses, args):
    assert ses != None and sessao.aberta(ses)

    id_ses = args['id_sessao']
    ses_exit = sessao.busca_por_identificador(id_ses)

    # Se for fechar a sessao ativa, feito logout
    if ses == ses_exit:
        sessao.fecha(ses)
        ses_nova = None
        pag = html_pag_principal.gera(ses_nova, None)
    # caso nao seja a sessao ativa, somente fecha e retorna para pagina de sessoes
    else:
        sessao.fecha(ses)
        ses_nova = None
        pag = html_pag_principal.gera(ses_nova, None)

    return pag, ses_nova
""" TENTATIVA DE IMPLEMENTAÇÃO PARA SESSAO NAO ATIVA
    else:
        sessao.fecha(ses_exit)]
        pag = html_pag_sessao.gera(ses,ses,None)
        ses_nova = ses
"""
