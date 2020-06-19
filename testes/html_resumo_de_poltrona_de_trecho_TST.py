import html_resumo_de_poltrona_de_trecho
import base_sql
import poltrona
import utils_testes
import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Inicializando módulo {poltrona}, limpando tabela:\n")
poltrona.inicializa(True)
sys.stderr.write("Criando testes do módulo {poltrona}\n")
poltrona.cria_testes()

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_resumo_de_poltrona_de_trecho
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

id_compra = "C-00000003"

testes = ( \
  ( "alT-coT-lvF-ofT", "A-00000001", "T-00000001", True,  True,   "C-00000003"), # Ocupada, oferta.
  ( "alT-coT-lvT-ofT", "A-00000002", "T-00000001", True,  True,   "C-00000003"), # Livre, oferta.
  ( "alT-coF-lvT-ofT", "A-00000002", "T-00000001", True,  False,  None        ), # Livre, oferta,
  ( "alF-coT-lvF-ofF", "A-00000003", "T-00000001", False, True,   "C-00000003"), # Ocupada, regular.
  ( "alF-coF-lvT-ofF", "A-00000004", "T-00000002", False, False,  None        ), # Livre, regular.
)

for rot, id_pol, id_trecho, alterar, comprar, id_comra in testes:
  pol = poltrona.busca_por_identificador(id_pol)
  testa(rot, pol, id_trecho, alterar, comprar, id_compra)
