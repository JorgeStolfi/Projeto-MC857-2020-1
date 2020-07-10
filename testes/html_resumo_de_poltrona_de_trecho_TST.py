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

testes = ( \
  ( "alT-coT-trF-lvF-ofT", "A-00000001", "T-00000001", True,  True,   False, "C-00000003"), # Ocupada, oferta.
  ( "alT-coT-trF-lvT-ofT", "A-00000002", "T-00000001", True,  True,   False, "C-00000003"), # Livre, oferta.
  ( "alT-coF-trF-lvT-ofT", "A-00000002", "T-00000001", True,  False,  False, None        ), # Livre, oferta,
  ( "alF-coT-trF-lvF-ofF", "A-00000003", "T-00000001", False, True,   False, "C-00000003"), # Ocupada, regular.
  ( "alF-coF-trF-lvT-ofF", "A-00000004", "T-00000002", False, False,  False, None        ), # Livre, regular.

  ( "alT-coT-trT-lvF-ofT", "A-00000001", "T-00000001", True,  True,   True,  "C-00000003"), # Ocupada, oferta.
  ( "alT-coT-trT-lvT-ofT", "A-00000002", "T-00000001", True,  True,   True,  "C-00000003"), # Livre, oferta.
  ( "alT-coF-trT-lvT-ofT", "A-00000002", "T-00000001", True,  False,  True,  None        ), # Livre, oferta,
  ( "alF-coT-trT-lvF-ofF", "A-00000003", "T-00000001", False, True,   True,  "C-00000003"), # Ocupada, regular.
  ( "alF-coF-trT-lvT-ofF", "A-00000004", "T-00000002", False, False,  True,  None        ), # Livre, regular.
)

for rot, id_pol, id_trc, alterar, comprar, trocar, id_cpr in testes:
  pol = poltrona.busca_por_identificador(id_pol)
  testa(rot, pol, id_trc, alterar, comprar, trocar, id_cpr)
