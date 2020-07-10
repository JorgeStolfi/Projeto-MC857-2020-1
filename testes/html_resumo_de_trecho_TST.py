#! /usr/bin/env python3

import html_resumo_de_trecho
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
tabelas.cria_todos_os_testes()

# Sessao de teste:
ses = sessao.busca_por_identificador("S-00000001")
assert ses != None

# Usuario teste:
usr1 = sessao.obtem_usuario(ses)
assert usr1 != None
usr1_id = usuario.obtem_identificador(usr1)
usr1_atrs = usuario.obtem_atributos(usr1)

# Trecho teste
trc1 = trecho.busca_por_identificador("T-00000001")
assert trc1 != None

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_resumo_de_trecho
  funcao = modulo.gera

  # testes unitários de tipo
  res = funcao(*args)
  assert type(res) is tuple or type(res) is list
  for campo in res:
    assert type(campo) is str

  # Teste da função {gera} HTML
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Testes com erros em vários formatos:
for rotulo, bt_ver, bt_alterar, bt_clonar, bt_fechar in ( \
    ("vN-aN-cN-fN", False, False, False, False), 
    ("vT-aN-cN-fN", True,  False, False, False), 
    ("vN-aT-cN-fN", False, True , False, False), 
    ("vT-aT-cN-fN", True,  True , False, False), 

    ("vN-aN-cT-fN", False, False, True , False), 
    ("vT-aN-cT-fN", True,  False, True , False), 
    ("vN-aT-cT-fN", False, True , True , False), 
    ("vT-aT-cT-fN", True,  True , True , False), 

    ("vN-aN-cN-fT", False, False, False, True ), 
    ("vT-aN-cN-fT", True,  False, False, True ), 
    ("vN-aT-cN-fT", False, True , False, True ), 
    ("vT-aT-cN-fT", True,  True , False, True ), 

    ("vN-aN-cT-fT", False, False, True , True ), 
    ("vT-aN-cT-fT", True,  False, True , True ), 
    ("vN-aT-cT-fT", False, True , True , True ), 
    ("vT-aT-cT-fT", True,  True , True , True ), 
 ):
  testa(rotulo, trc1, bt_ver, bt_alterar, bt_clonar, bt_fechar)
