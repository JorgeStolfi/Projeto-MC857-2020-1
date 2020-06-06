#! /usr/bin/python3

from utils_testes import erro_prog, aviso_prog
import html_pag_ver_usuario
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
ses = sessao.busca_por_identificador("S-00000004")
assert ses != None

# Usuario teste:
#usr1 = sessao.obtem_usuario(ses)
usr1 = usuario.busca_por_identificador("U-00000001")
assert usr1 != None
usr1_id = usuario.obtem_identificador(usr1)
usr1_atrs = usuario.obtem_atributos(usr1)

# Trecho teste
trecho1 = trecho.busca_por_identificador("T-00000001")
assert trecho1 != None

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_pag_ver_usuario
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Testes com erros em vários formatos:
for tag, erros in (
    ("N", None),
    ("V", []),
    ("E", ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",])
  ):
  rotulo = tag
  testa(rotulo, ses, usr1, erros)
