# Implementação do módulo {comando_solicitar_pag_ofertas}. 

import html_pag_ofertas
import poltrona
import trecho
import sessao

def processa(ses, args):
  id_poltronas = poltrona.busca_ofertas()
  poltronas = [poltrona.busca_por_identificador(id) for id in id_poltronas]
  id_trechos = list(set([poltrona.obtem_atributo(pol, 'id_trecho') for pol in  poltronas]))
  trechos = [trecho.busca_por_identificador(id) for id in id_trechos]
  pag = html_pag_ofertas.gera(ses, trechos, None)
  return pag
    
