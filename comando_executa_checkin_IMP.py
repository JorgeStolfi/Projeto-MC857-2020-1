import poltrona
import sessao
import html_pag_poltrona
import html_pag_mensagem_de_erro

def processa(ses, args):

  assert ses != None and sessao.eh_administrador(ses) # Paranóia.

  # Obtem a poltrona a fazer cehckin:
  id_pol = args['id_poltrona'] if 'id_poltrona' in args else None
  assert id_pol != None # Paranoia (formulário deve incluir este dado)
  pol = poltrona.busca_por_identificador(id_pol)
  
  # A poltrona deve estar reservada para alguma compra:
  assert poltrona.obtem_atributo(pol, 'id_compra') != None
  try:
    poltrona.muda_atributos(pol, { 'fez_checkin': True })
    pag = html_pag_poltrona.gera(ses, pol, None, None)
  except ErroAtrib as ex:
    erros = ex[0]
    # Mostra os dados da poltrona:
    pag = html_pag_poltrona.gera(ses, pol, None, erros)
  return pag
