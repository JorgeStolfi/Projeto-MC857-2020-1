#! /usr/bin/python3
 

import base_sql
import html_form_dados_de_compra
import tabelas
import compra
import usuario
import utils_testes
from utils_testes import erro_prog, aviso_prog
import sys

# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

# ----------------------------------------------------------------------
sys.stderr.write("Testando função...\n")
def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_form_dados_de_compra
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# pega admin
admin = usuario.busca_por_identificador('U-00000003')

# pega compra
compra1 = compra.busca_por_identificador('C-00000001')

# testa modulo
editavel = True
testa("edT", compra1, editavel, "Alterar", 'alterar_compra' )

editavel = False
testa("edF", compra1, editavel, "Alterar", 'alterar_compra' )
