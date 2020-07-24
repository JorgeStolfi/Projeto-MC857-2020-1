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
import html_form_table
import html_form
from utils_testes import erro_prog, aviso_prog
import sys

from trecho import obtem_atributos, obtem_poltronas

def gera(ses, trc, comprar_pols, alterar_trc, ver_oferta_pols, ver_fez_checkin,\
         checkin_pols, erros):

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
  atrs = trecho.obtem_atributos(trc)

  # Dados gerais do trecho:
  dados_linhas = [
    ( "Código",           "text",       "codigo",         "XX NNNN",                True, ),
    ( "Origem",           "text",       "origem",         "XXX",                    True, ),
    ( "Dia de partida",   "text",       "dia_partida",    "YYYY-MM-DD",             True, ),
    ( "Hora de partida",  "text",       "hora_partida",   "HH:MM",                  True, ),
    ( "Destino",          "text",       "destino",        "XXX",                    True, ),
    ( "Dia de chegada",   "text",       "dia_chegada",    "YYYY-MM-DD",             True, ),
    ( "Hora de chegada",  "text",       "hora_chegada",   "HH:MM",                  True, ),
    ( "Veículo",          "text",       "veiculo",        "XXX-NNNN",               True, ),
    ( "Poltronas",        "text",       "poltronas",      "1A-20D,33: 90.00; ...",  True, ),
    ( "Disponível",       "checkbox",   "aberto",         None,                     True, ),
  ]

  # Monta a tabela com os fragmentos HTML:
  ht_table = html_form_table.gera(dados_linhas, atrs, True)
  ht_form = html_form.gera(ht_table)

  

  # Lista de poltronas:
  pols_ids = poltrona.busca_por_trecho(trc)
  alterar_pols = alterar_trc
  sys.stderr.write(" pols_ids = %s\n" % str(pols_ids))
  sys.stderr.write(" id_trc = %s\n" % str(id_trc))
  sys.stderr.write(" alterar_pols = %s\n" % str(alterar_pols))
  sys.stderr.write(" comprar_pols = %s\n" % str(comprar_pols))
  sys.stderr.write(" id_cpr = %s\n" % str(id_cpr))
  ht_pols = html_lista_de_poltronas_de_trecho.gera(pols_ids, id_trc, \
    alterar_pols, comprar_pols, ver_oferta_pols, ver_fez_checkin, checkin_pols, id_cpr)
  ht_conteudo = ht_form + "<br/>" + ht_pols
  return html_pag_generica.gera(ses, ht_conteudo, erros)
