#! /usr/bin/python3

# Interfaces usadas por este script:

import base_sql
import usuario
from utils_testes import erro_prog, aviso_prog, mostra
import comando_cadastrar_usuario

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

ok_global = True # Vira {False} se um teste falha.
# ----------------------------------------------------------------------
# Função de teste:

def verifica_cadastrar_usuario(ses, dados, deveria_cadastrar):
  global ok_global

  comando_cadastrar_usuario.processa(ses, dados)

  usuarioResponse = usuario.busca_por_email(dados["email"])
  
  if (usuarioResponse != None and (not deveria_cadastrar)):
    ok_global = False
    aviso_prog("Cadastrou usuario quando não deveria cadastrar", True)

  if (usuarioResponse == None and deveria_cadastrar):
    ok_global = False
    aviso_prog("Não cadastrou usuario quando deveria cadastrar", True)

# ----------------------------------------------------------------------
# Executa chamadas
dados1 = {
    'nome': "Luiz Primeiro", 
    'senha': "123456789", 
    'conf_senha': "123456789",
    'email': "luiz@primeiro.com", 
    'CPF': "456.456.123-00", 
    'telefone': "+55(19)9 1324-5432",
    'documento': "1.432.567-9 SSP-SP",
    'administrador': False,
  }
verifica_cadastrar_usuario(None, dados1, True)
dados2 = {
    'nome': "Luiz Segundo", 
    'senha': "123456789", 
    'conf_senha': "987654321",
    'email': "luiz@segundo.com", 
    'CPF': "456.456.432-00", 
    'telefone': "+55(19)9 1324-1234",
    'documento': "1.987.567-9 SSP-SP",
    'administrador': False,
  }
verifica_cadastrar_usuario(None, dados2, False)
dados3 = {
    'nome': "Luiz Terceiro", 
    'senha': "123456789", 
    'conf_senha': "123456789",
    'email': "luiz@primeiro.com", 
    'CPF': "456.752.143-00", 
    'telefone': "+55(19)9 4268-1438",
    'documento': "1.432.746-9 SSP-SP",
    'administrador': True,
  }
verifica_cadastrar_usuario(None, dados3, True)
dados4 = {
    'nome': "Luiz Quarto", 
    'senha': "123456789", 
    'conf_senha': "987654321",
    'email': "luiz@segundo.com", 
    'CPF': "456.456.432-00", 
    'telefone': "+55(19)9 1945-1234",
    'documento': "1.132.567-9 SSP-SP",
    'administrador': True,
  }
verifica_cadastrar_usuario(None, dados4, False)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
