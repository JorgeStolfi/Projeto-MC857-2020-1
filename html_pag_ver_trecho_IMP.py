import html_pag_generica
import html_paragrafo
import html_table
import html_lista_de_poltronas_de_trecho
import html_resumo_de_trecho
import html_botao_simples
import html_botao_submit
import poltrona
import sessao
import compra
import trecho
from utils_testes import erro_prog, aviso_prog
import sys

from trecho import obtem_atributos, obtem_poltronas

def gera(ses, trc, comprar_pols, alterar_trc, erros):

  if comprar_pols:
    assert (ses != None) and (not sessao.eh_administrador(ses)) # Paranóia.
    cpr = sessao.obtem_carrinho(ses)
    id_cpr = compra.obtem_identificador(cpr)
  else:
    id_cpr = None

  if alterar_trc:
    assert sessao.eh_administrador(ses) # Paranóia.

  # Idenfiticadores do trecho e do carrinho:
  id_trc = trecho.obtem_identificador(trc)

  # Dados gerais do trecho:
  alterar_trc = alterar_trc
  clonar_trc = alterar_trc
  fechar_trc = alterar_trc
  linha_resumo = html_resumo_de_trecho.gera \
    (trc, False, alterar_trc, clonar_trc, fechar_trc)
  ht_resumo = " ".join(linha_resumo)

  # Lista de poltronas:
  pols_ids = poltrona.busca_por_trecho(trc)
  alterar_pols = alterar_trc
  sys.stderr.write(" pols_ids = %s\n" % str(pols_ids))
  sys.stderr.write(" id_trc = %s\n" % str(id_trc))
  sys.stderr.write(" alterar_pols = %s\n" % str(alterar_pols))
  sys.stderr.write(" comprar_pols = %s\n" % str(comprar_pols))
  sys.stderr.write(" id_cpr = %s\n" % str(id_cpr))
  ht_pols = html_lista_de_poltronas_de_trecho.gera(pols_ids, id_trc, alterar_pols, comprar_pols, id_cpr)
  ht_conteudo = ht_resumo + "<br/>" + ht_pols
  return html_pag_generica.gera(ses, ht_conteudo, erros)
