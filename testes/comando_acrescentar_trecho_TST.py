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

def testa_acrescenta_trecho_com_sucesso(id_trecho_ult, id_trecho_prox):
  """Testa a criação de um novo trecho com sucesso, dados
  o maior identificador válido {id_trecho_ult} e o menor inválido {id_trecho_prox}."""
  assert trecho.busca_por_identificador(id_trecho_ult) != None
  assert trecho.busca_por_identificador(id_trecho_prox) == None

  args = {
     'codigo': "AZ 2345",
     'origem': "SDU",
     'destino': "GRU",
     'dia_partida': "2020-05-25",
     'hora_partida': "13:40",
     'dia_chegada': "2020-05-26",
     'hora_chegada': "06:23",
     'veiculo': "jegue003",
     'poltronas': "1A-12D: 90.00",
  }
  testa("Suc", ses, args)

  trc_novo = trecho.busca_por_identificador(id_trecho_prox)
  assert trc_novo != None
  atrs_novo = trecho.obtem_atributos(trc_novo)
  assert atrs_novo == args

def testa_acrescenta_trecho_invalido(id_trecho_ult, id_trecho_prox):
  """Testa a criação de um novo trecho com falha, dados
  o maior identificador válido {id_trecho_ult} e o menor inválido {id_trecho_prox}."""
  assert trecho.busca_por_identificador(id_trecho_ult) != None
  assert trecho.busca_por_identificador(id_trecho_prox) == None

  args = {
     'codigo': "AZ 2345",
     'origem': "SDU",
     'dia_partida': "2020-05-25",
     'hora_partida': "13:40",
     'dia_chegada': "2020-05-26",
     'hora_chegada': "06:23",
  }
  testa("Inv", ses, args)
  trc_novo = trecho.busca_por_identificador(id_trecho_prox)
  assert trc_novo == None

testa_acrescenta_trecho_com_sucesso("T-00000006", "T-00000007")
testa_acrescenta_trecho_invalido("T-00000007", "T-00000008")
