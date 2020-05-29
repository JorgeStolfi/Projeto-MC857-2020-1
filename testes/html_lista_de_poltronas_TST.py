import html_lista_de_poltronas
import base_sql
import tabelas
import poltrona
import utils_testes
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

pol1_id = "A-00000001"
pol2_id = "A-00000002"
pol3_id = "A-00000003"
pol4_id = "A-00000004"
pol5_id = "A-00000005"
pol6_id = "A-00000006"
pol7_id = "A-00000007"
pol8_id = "A-00000008"

ses = sessao.busca_por_identificador("S-00000001")
cpr = compra.busca_por_identificador("C-00000002")

pols_ids = [pol1_id, pol2_id, pol3_id, pol4_id, pol5_id, pol6_id, pol7_id, pol8_id]

testa("F", ses, None, None, pols_ids, False)
testa("T", ses, cpr, None, pols_ids, True) # !!! USAR UMA LISTA DE COMPRAS DA SESSÃO !!!
