#! /usr/bin/python3

import comando_fechar_sessao
import base_sql
import tabelas
import usuario
import sessao
import compra
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando objetos...\n")
tabelas.cria_todos_os_testes()

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = comando_fechar_sessao
  funcao = modulo.processa
  frag = False
  pretty = False
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)
  
id_ses1 = "S-00000001" # Sessao do usuário fechador.
ses1 = sessao.busca_por_identificador(id_ses1)
assert ses1 != None
assert sessao.aberta(ses1)

for rotulo, ses, args in [ \
    # ('Sessão inexistente',          ses1,    {'id_sessao' : ''}) Não está implementado um tratamento para sessão inexistente
    ('Sessão existente',            ses1,    {'id_sessao' : 'S-00000002'}),
    ('Sessão do próprio usuário',   ses1,    {'id_sessao' : 'S-00000001'}),
    ('Sessão atual fechada',        ses1,    {'id_sessao' : 'S-00000003'})
  ]:
  testa(rotulo, ses, args)
