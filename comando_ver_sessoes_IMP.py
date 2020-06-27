# Implementação do módulo {comando_solicitar_pag_minhas_compras}.

import html_lista_de_compras
import html_pag_generica
import html_pag_mensagem_de_erro
import sessao
import usuario

import secrets

def processa(ses, args):
    assert ses != None
    pag = html_pag_mensagem_de_erro.gera(ses, "sessão corrente")
    assert sessao.aberta(ses)
    usr = sessao.obtem_usuario(ses)
    assert usr != None
    id_usr = usuario.obtem_identificador(usr)
    ids_sessoes = sessao.busca_por_identificador(id_usr)
    ht_conteudo = html_lista_de_sessoes.gera(ids_sessoes)
    pag = html_pag_generica.gera(ses, ht_conteudo, None)
    return pag
