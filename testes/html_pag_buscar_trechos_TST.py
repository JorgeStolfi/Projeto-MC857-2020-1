#! /usr/bin/python3

import html_pag_buscar_trechos
import tabelas
import usuario
import sessao
import trecho
import base_sql
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

# Sessao de teste:
ses = sessao.busca_por_identificador("S-00000001")
assert ses != None

# Usuario teste:
usr1 = sessao.obtem_usuario(ses)
assert usr1 != None
usr1_id = usuario.obtem_identificador(usr1)
usr1_atrs = usuario.obtem_atributos(usr1)

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_pag_buscar_trechos
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

atrs_vazio = {}.copy()
atrs_portos = { 'origem': "GRU", 'destino': "SDU" }
atrs_dias = { 'origem': "GRU", 'dia_min': "2020-05-06", 'dia_max': "2020-05-09" }

for admin in (False, True):
  ad = "-a" + str(admin)
  testa("N-e0" + ad, ses, atrs_vazio,  admin, None)              # Sem defaults
  testa("P-e0" + ad, ses, atrs_portos, admin, None)              # Com defaults
  testa("P-e1" + ad, ses, atrs_portos, admin, "Tente novamente") # Com defaults (portos) e erro
  testa("D-e0" + ad, ses, atrs_dias,   admin, None)              # Com defaults (origem e dias)
