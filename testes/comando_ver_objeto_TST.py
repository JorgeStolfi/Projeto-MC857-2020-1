#! /usr/bin/python3

# Interfaces usadas por este script:

import base_sql
import tabelas
import usuario
import sessao
import compra
import utils_testes; from utils_testes import erro_prog, aviso_prog, mostra
import comando_ver_objeto

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Obtem uma sessao de um usuario que é de administrador:
ses1 = sessao.busca_por_identificador("S-00000004")
assert sessao.eh_administrador(ses1)

ok_global = True # Vira {False} se um teste falha.
# ----------------------------------------------------------------------
# Função de teste:

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = comando_ver_objeto
  funcao = modulo.processa
  frag = False
  pretty = False
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)
  
for tag, id in ( \
    ("U", "U-00000001"),
    ("S", "S-00000001"),
    ("T", "T-00000001"),
    ("C", "C-00000001"),
    ("A", "A-00000001"),
  ):
  testa(tag, ses1, {'id': id})

# ----------------------------------------------------------------------
# Veredito final:
if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
