import html_resumo_de_poltrona
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

  modulo = html_resumo_de_poltrona
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


pol1_id = "A-00000001"
pol2_id = "A-00000002"
pol3_id = "A-00000003"
pol4_id = "A-00000004"

pol1 = poltrona.busca_por_identificador(pol1_id)
pol2 = poltrona.busca_por_identificador(pol2_id)
pol3 = poltrona.busca_por_identificador(pol3_id)
pol4 = poltrona.busca_por_identificador(pol4_id)

testa("pol_1", pol1, True, True)
testa("pol_2", pol2, True, False)
testa("pol_3", pol3, False, True)
testa("pol_4", pol4, False, False)
