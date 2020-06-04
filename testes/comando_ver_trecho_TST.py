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

sys.stderr.write("Criando objetos...\n")
tabelas.cria_todos_os_testes()

ses = sessao.busca_por_identificador("S-00000001")

trecho1 = trecho.busca_por_identificador("T-00000002")

#trecho1 = "T-00000001"
args = { 'id_trecho': trecho1 }
#trechoTest = comando_ver_trecho.processa("S-00000001", args)
trechoTest = comando_ver_trecho.processa(ses, args)


if trechoTest == trc :
  sys.stderr.write("Nao houve erros\n")
else:
  erro_prog(" : teste falhou")
