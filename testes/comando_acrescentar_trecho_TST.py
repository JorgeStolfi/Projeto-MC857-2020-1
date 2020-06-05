#! /usr/bin/python3

import comando_acrescentar_trecho
import tabelas
import trecho
import usuario
import sessao
import base_sql
import utils_testes

import sys

# Conecta ao banco de dados
sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Sessao para teste
ses = sessao.busca_por_identificador("S-00000001")

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = comando_acrescentar_trecho
  funcao = modulo.processa
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# !!! CONSERTAR !!! 

def testa_acrescenta_trecho_com_sucesso():
  args = {
     'codigo': "AZ 2345",
     'origem': "SDU",
     'destino': "GRU",
     'dia_partida': "2020-05-25",
     'hora_partida': "13:40",
     'dia_chegada': "2020-05-26",
     'hora_chegada': "06:23",
  }
  testa("Suc", ses, args)

  trc_novo = trecho.busca_por_identificador("T-00000004")
  atrs_novo = trecho.obtem_atributos(trc_novo)
  # assert atrs_novo == args 

def testa_acrescenta_trecho_invalido():
  args = {
     'codigo': "AZ 2345",
     'origem': "SDU",
     'dia_partida': "2020-05-25",
     'hora_partida': "13:40",
     'dia_chegada': "2020-05-26",
     'hora_chegada': "06:23",
  }
  testa("Inv", ses, args)
  trc_novo = trecho.busca_por_identificador("T-00000005")
  assert trc_novo == None

testa_acrescenta_trecho_com_sucesso()
testa_acrescenta_trecho_invalido()
