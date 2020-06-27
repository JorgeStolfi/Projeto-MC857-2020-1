# Implementação do módulo {comando_comprar poltrona}.

import poltrona
import compra

def processa(ses, args):
  usr_ses = sessao.obtem_usuario(ses)
  assert usr_ses is not None

  id_pol = args["id_pol"]
  assert id_pol is not None, "id_pol obrigatório para comprar"
  args.pop("id_pol")

  # Muda a poltrona para comprada
  pol = poltrona.busca_por_identificador(id_pol)
  poltrona.muda_atributos(pol, { 'OFERTA': False })

  compra.cria(usr_ses, "")

  # TODO: implementar
  pag = html_pag_comprar_poltrona.gera(ses)
  return pag
