import objeto
import trecho
import poltrona

import html_label
import html_input
import html_table
import html_botao_submit
import html_botao_simples
import html_form_table
import html_form
import html_imagem
from utils_testes import erro_prog, mostra
import sys
import os.path

def gera(id_trecho, atrs, texto_bt, comando_bt):
  if id_trecho != None:
    # Supõe que é mostrar trecho existente:
    # Inclui campo 'id_trecho' no formulário:
    ht_id_trecho = html_input.gera(None, "hidden", "id_trecho", id_trecho, None, True, None, None)
  else:
    # Supõe que é criação de novo trecho, ou buscar:
    alterar = False
    ht_id_trecho = ""

  if atrs == None: atrs = {}.copy() # Por via das dúvidas.
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
    ( "Aberto",       "checkbox",       "aberto",         None,                     True, ),
  ]

  # Monta a tabela com os fragmentos HTML:
  ht_table = html_form_table.gera(dados_linhas, atrs, True)

  ht_bt_acao = html_botao_submit.gera(texto_bt, comando_bt, None, '#55ee55')

  ht_bt_cancelar = html_botao_simples.gera("Cancelar", 'principal', None, '#ff2200')

  ht_conteudo = \
    ( "    " + ht_id_trecho + "\n" if ht_id_trecho != "" else "") + \
    ( ht_table + "\n" ) + \
    ( "    " + ht_bt_acao + "\n" ) + \
    ( "    " + ht_bt_cancelar + "\n" )

  ht = html_form.gera(ht_conteudo)

  if 'codigo' in atrs:
    cod_empresa = atrs['codigo'].split()[0]
    if os.path.isfile('imagens/' + cod_empresa + '.png'):
      img_empresa = html_imagem.gera('/' + cod_empresa + '.png', 'Logotipo empresa ' + cod_empresa, 200)
      return img_empresa + '<br clear="all" />' + ht

  return ht
