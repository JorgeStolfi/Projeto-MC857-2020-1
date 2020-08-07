import sessao
import usuario
import compra

import html_pag_compra
import html_pag_mensagem_de_erro

def processa(ses, args):

  # Obtém id da compra a alterar
  id_cpr = args['id_compra'] if 'id_compra' in args else None
  assert id_cpr != None # Paranóia (formulário deve incluir sempre).
  del args['id_compra']
  cpr = compra.busca_por_identificador(id_cpr)
  assert cpr != None # Paranóia.

  # Obtem dados alteráveis dos {args}:
  nome_pass = args['nome_pass'] if 'nome_pass' in args else None
  doc_pass = args['doc_pass'] if 'doc_pass' in args else None
  status = args['status'] if 'status' in args else None

  # Monta dicionário com alterações:
  novos_atrs = {}.copy()
  if nome_pass != None: novos_atrs['nome_pass'] = nome_pass
  if doc_pass != None: novos_atrs['doc_pass'] = doc_pass
  if status != None: novos_atrs['status'] = status

  # Editar passageiro
  try:
    compra.muda_atributos(cpr, novos_atrs)

    # Mostra compra com os novos valores
    pag = html_pag_compra.gera(ses, cpr, None, None)

  except ErroAtrib as ex:
    # Repete o formulário de alteração com valores já alterados e erros
    erros = ex[0]
    pag = html_pag_compra.gera(ses, cpr, args, erros)
  return pag
