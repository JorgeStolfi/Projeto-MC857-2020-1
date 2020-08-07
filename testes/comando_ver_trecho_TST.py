#! /usr/bin/python3

import sys
import base_sql
import tabelas
import sessao
import usuario
import utils_testes
import comando_ver_trecho

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando objetos...\n")
tabelas.cria_todos_os_testes(False)

ses_nao_admin = sessao.busca_por_identificador("S-00000001")
admin = usuario.busca_por_identificador("U-00000003")
ses_admin = sessao.cria(admin, "NOPQRSTUVWX", None)

args = { 'id_trecho' : "T-00000001"}

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = comando_ver_trecho
  funcao = modulo.processa
  frag = False
  pretty = False
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa("sem sessao", None, args)  # teste da pagina sem sessao
testa("trecho 1", ses_nao_admin, args) # teste da pagina com sessao de nao administrador, vendo trecho 1
testa("trecho 1 com admin", ses_admin, args) # teste da pagina com sessao de administrador, vendo trecho 1
