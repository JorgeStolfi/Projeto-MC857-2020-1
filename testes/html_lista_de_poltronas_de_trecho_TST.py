import html_lista_de_poltronas_de_trecho
import base_sql
import tabelas
import utils_testes

import usuario
import compra
import trecho
import sessao
import poltrona

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_lista_de_poltronas_de_trecho
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testes = ( \
  ( "U-00000001", "T-00000001", ), # Cliente comum.
  ( "U-00000001", "T-00000002", ), # Cliente comum.
  ( "U-00000003", "T-00000003"  ), # Admin.
  ( "U-00000003", "T-00000004", ), # Admin.
  ( None,         "T-00000005", ), # Usuario deslogado.

)
for usr_id, trc_id in testes:
  usr = None if usr_id == None else usuario.busca_por_identificador(usr_id)
  admin = False if usr == None else usuario.obtem_atributo(usr, 'administrador')
  usr_cprs = [] if usr == None else usuario.compras_abertas(usr)
  carr = None if len(usr_cprs) == 0 else usr_cprs[0] # Faz de conta que a primeira compra é o carrinho.
  id_carr = None if carr == None else compra.obtem_identificador(carr)
  
  trc = None if trc_id == None else trecho.busca_por_identificador(trc_id)
  assert trc != None
  ids_pols = trecho.obtem_poltronas(trc);

  rot = trc_id + "-" + str(usr_id) + "-" + str(id_carr)
  rot += "-admin" + str(admin)[0];
  rot += "-fzck" + str(fazer_checkin)[0];
  testa(rot, ids_pols, usr, carr)
