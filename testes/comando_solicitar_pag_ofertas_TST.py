import comando_solicitar_pag_ofertas
import base_sql
import tabelas
import usuario
import sessao
import utils_testes
import poltrona

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

sessions = [
  sessao.busca_por_identificador("S-00000001"),
  sessao.busca_por_identificador("S-00000002"),
  sessao.busca_por_identificador("S-00000003"),
  None
]

args = [
  "Lista de ofertas para a sessão S-00000001",
  "Lista de ofertas para a sessão S-00000002",
  "Lista de ofertas para a sessão S-00000003",
  "Lista de ofertas para a sessão Anônima",
]

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = comando_solicitar_pag_ofertas
  funcao = modulo.processa
  frag = False
  pretty = False
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

for ses, msg in zip(sessions, args):
  test_id = sessao.obtem_identificador(ses)[-1] if ses != None else '0'
  testa("T-" + test_id, ses, msg)
