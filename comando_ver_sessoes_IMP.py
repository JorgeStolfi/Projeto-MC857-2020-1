# Implementação do módulo {comando_solicitar_pag_minhas_compras}.

import html_lista_de_sessoes
import html_pag_generica
import html_pag_mensagem_de_erro
import sessao
import usuario

# args recebe id do usuario que eu quero checar a sessao.
def processa(ses, args):
    assert ses != None
    pag = html_pag_mensagem_de_erro.gera(ses, "sessão corrente")
    assert sessao.aberta(ses)
    usr = sessao.obtem_usuario(ses)
    assert usr != None
    
    ids_sessoes = sessao.busca_por_usuario(args['id'])
    
    ht_conteudo = html_lista_de_sessoes.gera(ids_sessoes)
    pag = html_pag_generica.gera(ses, ht_conteudo, None)
    return pag
