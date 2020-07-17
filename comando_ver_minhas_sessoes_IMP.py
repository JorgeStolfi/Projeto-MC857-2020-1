# Implementação do módulo {comando_solicitar_pag_minhas_compras}.

import html_lista_de_sessoes
import html_pag_generica
import sessao
import usuario

def processa(ses, args):
    assert ses != None
    assert sessao.aberta(ses)

    # request para ver sessões do próprio user
    usr = sessao.obtem_usuario(ses)
    assert usr != None

    # com o id do usuário da sessao, podemos buscar suas sessões no banco
    sessoes = usuario.sessoes_abertas(usr)
    ids_sessoes = []
    for i in sessoes:
        if (i != ses):
            ids_sessoes.append(sessao.obtem_identificador(i))

    ht_conteudo = html_lista_de_sessoes.gera(ids_sessoes, True, True)
    pag = html_pag_generica.gera(ses, ht_conteudo, None)
    
    return pag
