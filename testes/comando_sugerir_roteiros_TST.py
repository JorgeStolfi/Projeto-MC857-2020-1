#! /usr/bin/python3

import base_sql
import tabelas
import usuario
import sessao
import compra
import utils_testes; from utils_testes import erro_prog, aviso_prog, mostra
import comando_sugerir_roteiros

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

ok_global = True # Vira {False} se um teste falha.
# ----------------------------------------------------------------------
# Função de teste:

def testa_comando_sugerir_roteiros(dados, resultado):
  global ok_global

  modulo = comando_sugerir_roteiros
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
testa_comando_sugerir_roteiros(dados, True)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
