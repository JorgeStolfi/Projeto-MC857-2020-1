#! /usr/bin/python3

import html_pag_acrescentar_trecho
import tabelas
import usuario
import sessao
import base_sql
import utils_testes

import sys
 
sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Sessao de teste cujo usuario é admin:
ses = sessao.busca_por_identificador("S-00000004")
assert ses != None

form = {
  'origem': 'GRU',
  'destino': 'RAO',
  'dia_partida': '2020-05-02',
  'dia_chegada': '2020-05-02'
}

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_pag_acrescentar_trecho
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa("pag_acrescentar_trecho", ses, form, None)