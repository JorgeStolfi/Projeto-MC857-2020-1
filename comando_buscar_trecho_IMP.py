# Implementação do módulo {comando_buscar_trecho}.

import trecho
import html_bloco_lista_de_trechos
import html_pag_generica

from valida_campo import ErroAtrib

def processa(ses, args):
    try:
        ids_trechos = trecho.busca_por_origem_e_destino(args['destino'], args['origem'])
        bloco = html_bloco_lista_de_trechos.gera(ses, ids_trechos)
        pag = html_pag_generica.gera(ses, bloco, None)
        return pag

    except ErroAtrib as ex:
        erros = ex.args[0]
        # Repete a página sem o bloco e com mens de erro:
        pag = html_pag_generica.gera(ses, None, erros)
        return pag