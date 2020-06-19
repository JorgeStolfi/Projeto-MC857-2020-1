import html_lista_de_poltronas_de_trecho
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

  modulo = html_lista_de_poltronas_de_trecho
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

trc1_id = "T-00000001"
trc1 = trecho.busca_por_identificador(trc1_id)
trc1_pols_ids = poltrona.busca_por_trecho(trc1)

cpr1_id = "C-00000002"

testa("aF-cF", trc1_pols_ids, trc1_id, False, False, cpr1_id)
testa("aF-cT", trc1_pols_ids, trc1_id, False, True,  cpr1_id)
testa("aT-cF", trc1_pols_ids, trc1_id, True,  False, cpr1_id)
testa("aT-cT", trc1_pols_ids, trc1_id, True,  True,  cpr1_id)
