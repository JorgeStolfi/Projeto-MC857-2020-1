#! /usr/bin/python3

# Interfaces usadas por este script:

import base_sql
import tabelas
import usuario
import sessao
import compra
from utils_testes import erro_prog, aviso_prog, mostra
import comando_fazer_login

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

ok_global = True # Vira {False} se um teste falha.
# ----------------------------------------------------------------------
# Função de teste:

def verifica_login(email, senha, deveria_logar):
  global ok_global
  dados = {
    "email": email,
    "senha": senha
  }
  pag, ses = comando_fazer_login.processa(None, dados)

  if (deveria_logar and ses == None):
    ok_global = False
    aviso_prog("Não gerou a sessão quando deveria para o email " + str(email), True)

  if ((not deveria_logar) and ses != None):
    ok_global = False
    aviso_prog("Gerou gerou a sessão quando não deveria para o email " + str(email), True)

# ----------------------------------------------------------------------
# Executa chamadas
verifica_login("primeiro@gmail.com", "123456789", True)
verifica_login("nao_existo@gmail.com", "123456789", False)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
