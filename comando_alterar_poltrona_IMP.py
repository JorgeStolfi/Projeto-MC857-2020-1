import sessao
import usuario
import poltrona

import html_pag_poltrona
import html_pag_mensagem_de_erro

def processa(ses, args):

  # Determina se usuario é administrador
  assert sessao.eh_administrador(ses)
  
  # Obtem a poltrona: 
  id_poltrona = args['id_poltrona']
  assert id_poltrona != None # Paranóia (o formulário deve incluir).
  del args['id_poltrona']
  pol = poltrona.busca_por_identificador(id_poltrona)
  assert pol != None # Paranóia.
  pol_atrs = poltrona.obtem_atributos(pol)
  
  id_trecho = args['id_trecho']
  assert id_trecho == pol_atrs['id_trecho'] # Deve ser readonly no form.
  
  id_compra = args['id_compra']
  assert id_compra == pol_atrs['id_compra'] # Deve ser readonly no form.

  numero = args['numero']
  assert numero == pol_atrs['numero'] # Deve ser readonly no form.
 
  # Monta dicionário com alterações:
  atrs_a_mudar = {}.copy()
  
  oferta = args['oferta'] if 'oferta' in args else None  # Alterável.
  if oferta != None and type(oferta) is str: oferta = (oferta == "on")
  if oferta != None: atrs_a_mudar['oferta'] = oferta
  
  preco = args['preco'] if 'preco' in args else None  # Alterável.
  if preco != None and type(preco) is str: preco = float(preco)
  if preco != None: atrs_a_mudar['preco'] = preco

  # Editar poltrona
  try:
    poltrona.muda_atributos(pol, atrs_a_mudar)
    # Mostra poltrona com dados alterados:
    pag = html_pag_poltrona.gera(ses, pol, None, None)

  except ErroAtrib as ex:
    # Mostra novamente a poltrona com mesmos args e mens de erro:
    erros = ex[0]
    pag = html_pag_poltrona.gera(ses, pol, args, erros)
  
  return pag
