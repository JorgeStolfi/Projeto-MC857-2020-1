import usuario
import compra
import sessao
import trecho
import poltrona

import html_pag_ver_usuario
import html_pag_ver_compra
import html_pag_ver_sessao
import html_pag_ver_trecho
import html_pag_ver_poltrona

import html_pag_mensagem_de_erro
import sys #added by shimeji


def processa(ses, args):
  # O dono da sessão deve ser administrador:
  assert sessao.eh_administrador(ses)
  
  # O dicionário {args} deve conter campo 'id':
  try:
    assert 'id' in args
    id = args['id']
    letra = id[0]
  except:
    return html_pag_mensagem_de_erro.gera(ses, "O identificador fornecido é inválido. Por favor, verifique se digitou corretamente e tente de novo.")

  try:
    if letra == "U":
      usr = usuario.busca_por_identificador(id)
      pag = html_pag_ver_usuario.gera(ses, usr, None)
    elif letra == "C":
      cpr = compra.busca_por_identificador(id)
      excluir_pols = False
      trocar_pols = False
      pag = html_pag_ver_compra.gera(ses, cpr, excluir_pols, trocar_pols, None)
    elif letra == "T":
      trc = trecho.busca_por_identificador(id)
      alterar_pols = True
      comprar_pols = False
      pag = html_pag_ver_trecho.gera(ses, trc, False, False, None)
    elif letra == "S":
      ses1 = sessao.busca_por_identificador(id)
      pag = html_pag_ver_sessao.gera(ses, ses1, None)
    elif letra == "A":
      excluir_pol = False
      id_cpr = None
      pol = poltrona.busca_por_identificador(id)
      pag = html_pag_ver_poltrona.gera(ses, pol, id_cpr, excluir_pol, None)
    else:
      pag = html_pag_mensagem_de_erro.gera(ses, "Classe de objeto \"" + letra + "\" inválida")
  except:
    return html_pag_mensagem_de_erro.gera(ses, "O identificador \"" + id + "\" não foi encontrado. Por favor, verifique se digitou corretamente e tente de novo.")
  return pag

