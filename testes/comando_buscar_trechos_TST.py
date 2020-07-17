#! /usr/bin/python3

import comando_buscar_trechos
import tabelas
import usuario
import sessao
import base_sql
import utils_testes

import sys

# Conecta no banco e carrega alimenta com as informações para o teste

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Sessao de teste
ses = sessao.busca_por_identificador("S-00000001")


def testa(rotulo, ses, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = comando_buscar_trechos
  pag = modulo.processa(ses, args[0])
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_modulo_html(modulo, rotulo, pag, frag, pretty)

# testa('vazio',      ses, {},                                           )
testa('1-None',            ses, { 'origem': None },                           )
testa('1-org',             ses, { 'origem': 'SDU' },                          )
testa('2-dst-dmin',        ses, { 'origem': 'SDU', 'dia_min': "2020-05-08" }, )

testa('3-org-dmax',        ses, {'origem': 'SDU', 'dia_chegada': "2020-05-08"})
testa('4-org-dhmax',       ses, {'origem': 'SDU', 'dia_chegada': "2020-05-08", 'hora_chegada': "20:30"})
testa('5-org-dmin',        ses, {'origem': 'SDU', 'dia_partida': "2020-05-08"})
testa('6-org-dhmin',       ses, {'origem': 'SDU', 'dia_partida': "2020-05-08", 'hora_partida': "16:00"})
testa('7-org-dmin-dmax',   ses, {'origem': 'SDU', 'dia_partida': "2020-05-08", 'dia_chegada': "2020-05-08"})
testa('8-org-dhmin-dhmax', ses, {
    'origem': 'SDU', 
    'dia_partida': "2020-05-08", 'hora_partida': "19:30",
    'dia_chegada': "2020-05-08", 'hora_chegada': "20:30"
  }
)
testa('9-dmin-dmax',       ses, {'dia_partida': "2020-05-08", 'dia_chegada': "2020-05-08"})
