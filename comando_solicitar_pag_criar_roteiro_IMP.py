# Implementação do módulo {comando_solicitar_pag_criar_roteiro}. 

import html_pag_criar_roteiro


def processa(ses, args):
    pag = html_pag_criar_roteiro.gera(ses)
    return pag
