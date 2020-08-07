import html_resumo_de_poltrona_de_usuario
import base_sql
import poltrona
import tabelas
import utils_testes
import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_resumo_de_poltrona_de_usuario
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testes = ( \
  ( "teste-um", "A-00000001"),
  ( "teste-dois", "A-00000003"),  
  ( "teste-tres", "A-00000006"),  
  ( "teste-quatro", "A-00000008"),
)

for rot, id_pol in testes:
  pol = poltrona.busca_por_identificador(id_pol)
  assert pol != None
  testa(rot, pol)