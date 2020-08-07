#! /usr/bin/python3

import html_pag_buscar_compras
import tabelas
import usuario
import sessao
import compra
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

  modulo = html_pag_buscar_compras
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


for admin in (False, True):
  ad = "-a" + str(admin)
  testa("N-e0" + ad, ses, {},                             admin, None) # Sem defaults
  testa("D-e0" + ad, ses, { 'id_usuario': "U-00000001" }, admin, None) # Com defaults
  testa("D-e1" + ad, ses, { 'id_usuario': "U-00000001"},  admin, "Tente novamente") # Com defaults e erro
