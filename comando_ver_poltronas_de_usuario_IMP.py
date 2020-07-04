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
  assert ses != None
  pag = html_pag_mensagem_de_erro.gera(ses, "sessão corrente")
  assert sessao.aberta(ses)
  ids_compras = compra.busca_por_cliente(args['id'])
  
  ids_poltronas = []
  for i in range(len(ids_compras)):
      cpr = compra.busca_por_identificador(ids_compras[i])
      ids_poltronas += poltrona.busca_por_compra(cpr)

  ht_conteudo = html_lista_de_poltronas_de_usuario.gera(ids_poltronas)
    
  pag = html_pag_generica.gera(ses, ht_conteudo, None)

  return pag