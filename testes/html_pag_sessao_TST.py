#! /usr/bin/python3

import html_pag_sessao
import base_sql
import utils_testes
import tabelas
import sessao
import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

# sessao do admin
ses = sessao.busca_por_identificador("S-00000001")

# sessao de teste
ses1 = sessao.busca_por_identificador("S-00000001")

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_pag_sessao
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa("S-E0", ses, ses1, None)
testa("S-E2", ses, ses1, ["Veja a mensagem abaixo", "Veja a mensagem acima"])
