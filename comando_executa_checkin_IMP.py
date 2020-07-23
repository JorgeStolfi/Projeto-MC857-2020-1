import poltrona
import sessao
import html_pag_ver_poltrona
import html_pag_mensagem_de_erro

def processa(ses, args):
  assert sessao.eh_administrador(ses)

  # Extrair dado de {args}
  try:
    # Obter id da poltrona
    id_poltrona = args['id_poltrona']
    assert id_poltrona is not None, 'id_poltrona obrigatório para fazer check-in'
  except KeyError as ex:
    return html_pag_mensagem_de_erro.gera(ses, ("** Erro ao extrair os dados do dicionario de argumentos. Verifique se os campos foram preenchidos**"))
  
  try:
    pol = poltrona.busca_por_identificador(id_poltrona)

    # Verifica que a poltrona esta reservada
    assert poltrona.obtem_atributo(pol, 'oferta') == False
    assert poltrona.obtem_atributo(pol, 'id_compra') != None

    # poltrona.muda_atributos(pol, { 'fez_checkin': True })
    pag = html_pag_ver_poltrona.gera(ses, pol, None, False, None)

  except:
    pag = html_pag_mensagem_de_erro.gera(ses, ("** Um erro ocorreu ao alterar a poltrona **"))
  
  return pag