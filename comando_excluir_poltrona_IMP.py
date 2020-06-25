# Implementação do módulo {comando_excluir_poltrona}.

import poltrona
import compra
import html_pag_ver_compra

def processa(ses, args):
    id_poltrona = args['id_poltrona']
    id_compra = args['id_compra']

    poltrona_a_ser_excluida = poltrona.busca_por_identificador(id_poltrona)

    cpr = compra.busca_por_identificador(id_compra)

    # Ao definir {id_compra} como {None}, estamos excluindo a poltrona
    poltrona.muda_atributos(poltrona_a_ser_excluida, {'id_compra': None})

    pag = html_pag_ver_compra.gera(ses, cpr, True, True, None)

    return pag