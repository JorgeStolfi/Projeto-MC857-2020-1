# Implementação do módulo {comando_ver_poltrona}.

import html_lista_de_poltronas_de_usuario
import html_pag_generica
import html_pag_mensagem_de_erro
import sessao
import usuario
import compra
import poltrona
import sys

def processa(ses, args):

  try:
    assert ses != None
    assert sessao.aberta(ses)
    assert 'id_user' or 'id_poltrona' in args
    id_user = args['id_user']
    id_poltrona = args['id_poltrona']
  except:
    return html_pag_mensagem_de_erro.gera(ses, "O identificador fornecido é inválido. Por favor, verifique se digitou corretamente e tente de novo.")

  if id_user:
    ids_compras = compra.busca_por_cliente(id_user)
    ids_poltronas = []
    for i in range(len(ids_compras)):
      cpr = compra.busca_por_identificador(ids_compras[i])
      ids_poltronas += poltrona.busca_por_compra(cpr)
    ht_conteudo = html_lista_de_poltronas_de_usuario.gera(ids_poltronas)
    pag = html_pag_generica.gera(ses, ht_conteudo, None)

  if id_poltrona:
    ids_poltronas = poltrona.busca_por_identificador("A-00000001")
    ht_conteudo = html_lista_de_poltronas_de_usuario.gera(ids_poltronas)
    pag = html_pag_generica.gera(ses, ht_conteudo, None)

  return pag