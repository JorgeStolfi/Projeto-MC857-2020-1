import html_form_dados_de_poltrona
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

  modulo = html_form_dados_de_poltrona
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

pol1_id = "A-00000001"
pol1 = poltrona.busca_por_identificador(pol1_id)
pol1_atrs = {}
pol1_id_cpr = None
testa("pol1_alterar_vazio", pol1_id, pol1_atrs, True,  False, False,  pol1_id_cpr)

pol2_id = "A-00000007"
pol2 = poltrona.busca_por_identificador(pol2_id)
pol2_atrs = { 'preco': 23.45, 'id_trecho': "T-00000231", 'numero': "99F" }
assert poltrona.obtem_atributo(pol2, 'id_compra') == None
pol2_id_cpr = None
testa("pol2_alterar_alguns", pol2_id, pol2_atrs, True,  False, False, None)

pol3_id = "A-00000003"
pol3 = poltrona.busca_por_identificador(pol3_id)
pol3_atrs = poltrona.obtem_atributos(pol3)
pol3_id_cpr = poltrona.obtem_atributo(pol3, 'id_compra')
testa("pol3_excluir_todos", pol3_id, pol3_atrs, False, False, True,  pol3_id_cpr)
testa("pol3_ver_todos",     pol3_id, pol3_atrs, False, False, False, pol3_id_cpr)

pol4_id = "A-00000007"
pol4 = poltrona.busca_por_identificador(pol4_id)
pol4_atrs = poltrona.obtem_atributos(pol4)
assert poltrona.obtem_atributo(pol4, 'id_compra') == None
pol4_id_cpr = "C-00000002"
testa("pol4_comprar_todos", pol4_id, pol4_atrs, False, True,  False, pol4_id_cpr)
