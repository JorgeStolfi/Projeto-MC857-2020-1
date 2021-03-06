import html_resumo_de_poltrona_de_compra
import base_sql
import poltrona
import tabelas
import utils_testes
import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_resumo_de_poltrona_de_compra
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testes = ( \
  ( "veT-exT", "A-00000001", "C-00000001", True,  True,  ),
  ( "veF-exF", "A-00000003", "C-00000002", False, False, ),  
  ( "veF-exT", "A-00000003", "C-00000002", False, True,  ),  
)

for rot, id_pol, id_compra, ver, excluir, in testes:
  pol = poltrona.busca_por_identificador(id_pol)
  assert pol != None
  testa(rot, pol, id_compra, ver, excluir)
