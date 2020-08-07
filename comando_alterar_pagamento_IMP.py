import sessao
import usuario
import compra

import html_pag_compra
import html_pag_mensagem_de_erro

def processa(ses, args):
  # Obtém a compra:
  id_cpr = args['id_compra']
  assert id_cpr is not None # Paranóia (formulário deve incluir).
  del args['id_compra']
  cpr = compra.busca_por_identificador(id_cpr)
  assert cpr != None  # Paranóia.

  # Obtém dados alterados:
  forma_pag = args['metodo']
  assert id_cpr is not None # Paranóia (formulário deve obrigar a preencher)

  # Aplica a compra:
  try:
    novos_atrs = {'forma_pag': forma_pag}
    compra.muda_atributos(cpr, novos_atrs)

    # Atualiza a pagina com os novos valores
    pag = html_pag_compra.gera(ses, cpr, None, None)

  except ErroAtrib as ex:
    # Repete a página da alterar compra com mesmos atributos e mens de erro:
    erros = ex[0]
    pag = html_pag_compra.gera(ses, cpr, args, erros)

  return pag
