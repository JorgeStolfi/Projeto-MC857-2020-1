import sys
import comando_relatorio_de_trafego
import base_sql
import tabelas
import sessao
import compra
import utils_testes; from utils_testes import erro_prog, mostra

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando objetos...\n")
tabelas.cria_todos_os_testes(False)

ses = sessao.busca_por_identificador("S-00000003")
args = None 

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = comando_relatorio_de_trafego
  funcao = modulo.processa
  frag = False
  pretty = False
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa("relatorio", ses, args)