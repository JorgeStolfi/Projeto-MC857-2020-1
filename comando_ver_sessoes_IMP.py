# Implementação do módulo {comando_solicitar_pag_minhas_compras}.

import html_lista_de_sessoes
import html_pag_generica
import html_pag_mensagem_de_erro
import sessao
import usuario

def processa(ses, args):

    assert ses != None
    assert sessao.aberta(ses)
    # request para ver sessões de outro user
    if 'id' in args:
        id_usr = args['id']
    # request para ver sessões do próprio user
    else:
        usr = sessao.obtem_usuario(ses)
        assert usr != None
        id_usr = usuario.obtem_identificador(usr)

    # com o id do usuário, podemos buscar suas sessões no banco
    ids_sessoes = sessao.busca_por_campo('usr', id_usr)
    ht_conteudo = html_lista_de_sessoes.gera(ids_sessoes)
    pag = html_pag_generica.gera(ses, ht_conteudo, None)
    return pag
