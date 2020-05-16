import html_bloco_lista_de_assentos
import base_sql
import tabelas
import assento
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
  
  modulo = html_bloco_lista_de_assentos
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

assento1_ident = "A-00000001"
assentto2_ident = "A-00000002"
assento3_ident = "A-00000003"
assento4_ident = "A-00000004"
asssento5_ident = "A-00000005"
assento6_ident = "A-00000006"
assento7_ident = "A-00000007"
assento8_ident = "A-00000008"

assento_indet_list = [assento1_ident, assentto2_ident, assento3_ident, assento4_ident,
 asssento5_ident, assento6_ident, assento7_ident, assento8_ident]

testa("Assentos", None, None, None, assento_indet_list, None)