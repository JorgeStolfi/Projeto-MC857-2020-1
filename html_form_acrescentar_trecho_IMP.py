
import objeto
import usuario
import trecho
import poltrona

from trecho import Objeto_Trecho

import tabela_generica
import tabelas
import conversao_sql
import identificador
import valida_campo; from valida_campo import ErroAtrib
from utils_testes import erro_prog, mostra
import sys

# Imports html_form_dados_de_usuario
import html_input
import html_botao_submit
import html_botao_simples
import html_form_tabela_de_campos
import html_form

def gera(atrs):
  # For simplicity:
  if atrs == None: atrs = {}.copy()

  # Dados brutos para as linhas. Para cada linha, o rótulo, tipo do "<input>", nome do campo, e dica.

  dados_linhas = (
      ( "Código",           "text",       "codigo",         "XX NNNN",                False, ),
      ( "Origem",           "text",       "origem",         "XXX",                    False, ),
      ( "Destino",          "text",       "destino",        "XXX",                    False, ),
      ( "Dia de partida",   "text",       "dia_partida",    "YYYY-MM-DD",             False, ),
      ( "hora de partida",  "text",       "hora_partida",   "HH:MM",                  False, ),
      ( "Dia de chegada",   "text",       "dia_chegada",    "YYYY-MM-DD",             False, ),
      ( "hora de chegada",  "text",       "hora_chegada",   "HH:MM",                  False, ),
  )

  ht_tabela = html_form_tabela_de_campos.gera(dados_linhas, atrs, True)

  ht_submit = html_botao_submit.gera("Acrescentar", "acrescentar_trecho", None, "#44ff00")

  ht_cancel = html_botao_simples.gera("Cancelar", 'principal', None, "#ff2200")

  ht_conteudo = ht_tabela + ht_submit + ht_cancel

  return html_form.gera(ht_conteudo)
