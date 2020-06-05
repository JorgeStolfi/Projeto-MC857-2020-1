import html_lista_de_poltronas
import base_sql
import tabelas
import poltrona
import utils_testes
import sessao
import compra
import trecho
import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_lista_de_poltronas
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

cpr = compra.busca_por_identificador("C-00000001")
cpr_pols_ids = poltrona.busca_por_compra(cpr)

testa("CPR", cpr_pols_ids, cpr, None, True)


trc = trecho.busca_por_identificador("T-00000001")
cpr_pols_ids = poltrona.busca_por_trecho(trc)

testa("TRC", cpr_pols_ids, None, trc, True)
