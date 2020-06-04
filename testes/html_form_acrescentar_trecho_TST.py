#! /usr/bin/python3
 

import html_form_acrescentar_trecho

import trecho
import sessao
import poltrona

import sys
import base_sql
import tabelas
import utils_testes

from utils_testes import erro_prog, aviso_prog


# mock bd
sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Testes da função gera(atrs)
def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_form_acrescentar_trecho
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


# Teste 01: {atrs} = {}
sys.stderr.write("# Teste 01: Nenhum atributo\n")
atrs = None
testa("vazio", atrs)

# Teste 02: {atrs} = {None}
sys.stderr.write("# Teste 02: Atributo codigo\n")
atrs = {"codigo":"12 333"}
testa("um_campo", atrs)

# Teste 03: 
sys.stderr.write("# Teste 02: Todos atributos\n")
atrs = {"codigo":"12 333",
        "origem":"111",
        "destino":"222",
        "dia_partida":"2020-05-29",
        "hora_partida":"15:30",
        "dia_chegada":"2020-05-29",
        "hora_chegada":"16:00",
        "poltronas":"1A-20D"}
testa("todos_campos", atrs)

# Teste 04: 
sys.stderr.write("# Teste 04: Atributos invalidos\n")
atrs = {"codigo":"abcdef",
        "origem":"abcdef",
        "destino":"abcdef",
        "dia_partida":"abcdef",
        "hora_partida":"abcdef",
        "dia_chegada":"abcdef",
        "hora_chegada":"abcdef",
        "poltronas":"abcdef"}
testa("todos_campos_invalidos", atrs)