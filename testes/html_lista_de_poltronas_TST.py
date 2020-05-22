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

poltrona1_ident = "A-00000001"
poltrona2_ident = "A-00000002"
poltrona3_ident = "A-00000003"
poltrona4_ident = "A-00000004"
poltrona5_ident = "A-00000005"
poltrona6_ident = "A-00000006"
poltrona7_ident = "A-00000007"
poltrona8_ident = "A-00000008"

poltrona_indet_list = [poltrona1_ident, poltrona2_ident, poltrona3_ident, poltrona4_ident,
 poltrona5_ident, poltrona6_ident, poltrona7_ident, poltrona8_ident]

testa("Poltronas", None, None, None, poltrona_indet_list, None)
