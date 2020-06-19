import html_lista_de_poltronas_de_compra
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

  modulo = html_lista_de_poltronas_de_compra
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

cpr1_id = "C-00000001"
cpr1 = compra.busca_por_identificador(cpr1_id)
cpr1_pols_ids = poltrona.busca_por_compra(cpr1)

testa("eF-tF", cpr1_pols_ids, cpr1_id, False, False)
testa("eF-tT", cpr1_pols_ids, cpr1_id, False, True )
testa("eT-tF", cpr1_pols_ids, cpr1_id, True,  False)
testa("eT-tT", cpr1_pols_ids, cpr1_id, True,  True )
