#! /usr/bin/python3

import sys
import comando_ver_trecho
import trecho
import base_sql
import tabelas
import sessao
from utils_testes import erro_prog, mostra

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

# !!! CONSERTAR !!!

sys.stderr.write("Criando objetos...\n")
tabelas.cria_todos_os_testes()

ses = sessao.busca_por_identificador("S-00000001")

trc1_id = "T-00000002"
trc1 = trecho.busca_por_identificador(trc1_id)

args = { 'id_trecho': trc1_id }
pag = comando_ver_trecho.processa(ses, args)

if pag == trc1:
  sys.stderr.write("Nao houve erros\n")
else:
  erro_prog(" : teste falhou")
