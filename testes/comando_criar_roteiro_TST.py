#! /usr/bin/python3

# Interfaces usadas por este script:

import base_sql
import tabelas
import usuario
import sessao
import compra
import utils_testes; from utils_testes import erro_prog, aviso_prog, mostra
import comando_criar_roteiro

import sys

ok_global = True # Vira {False} se um teste falha.
# ----------------------------------------------------------------------
# Função de teste:

def testa_comando_criar_roteiro(dados, resultado):
  global ok_global

  modulo = comando_criar_roteiro
  pag = modulo.processa(None, dados)

  if (resultado and pag == None):
    ok_global = False
    aviso_prog("Não devolveu a pagina quando deveria devolver", True)

  if ((not resultado) and pag != None):
    ok_global = False
    aviso_prog("Devolveu a pagina quando não deveria devolver", True)
    
# ----------------------------------------------------------------------
# Executa chamadas
dados = {
    "origem": "VCP",
    "destino": "POA",
    "dia_min": "2020-05-08",
    "dia_max": "2020-05-09"
}
testa_comando_criar_roteiro(dados, True)
dados = {}
testa_comando_criar_roteiro(dados, False)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
