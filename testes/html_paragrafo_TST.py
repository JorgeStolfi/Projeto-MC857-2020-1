#! /usr/bin/python3

# Interfaces usadas por este script:

import html_paragrafo; from html_paragrafo import *
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

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Testes das funções de {gera_html_elem}:

def testa(rotulo,  funcao, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/gera_html_elem.{rotulo}.html"."""

  modulo = html_paragrafo
  frag = True
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, *args)

ses = sessao.busca_por_identificador("S-00000001")
assert ses != None
assert sessao.aberta(ses)

usr = sessao.obtem_usuario(ses)
assert usr != None
unome = usuario.obtem_atributos(usr)['nome']

prod1_ident = "P-00000001"
# prod1 = produto.busca_por_identificador(prod1_ident)
prod2_ident = "P-00000002"
prod5_ident = "P-00000005"

cpr1_ident = "C-00000001"
cpr1 = compra.busca_por_identificador(cpr1_ident)

testa("N", span, "font-family: 'Courier'; font-size: 30px", "Hello World")

testa("N", div, "font-family: 'Courier'; font-size: 30px", "Hello World")

testa("N", paragrafo, "font-family: 'Courier'; font-size: 30px", "Hello World")

testa("N", bloco_texto, "inline-block", "Hello World","Helvetica","18px","bold","30px","center","#000000","#ff8800")

testa("1", input, "Rotulo", "text", "voltagem", None, "Voltagem Máxima", "testa_input")
testa("2", input, "Rotulo", "text", "voltagem", "30 V", None, "testa_input")

testa("T", label, "Rotulo", ": ")
testa("N", label, None, ": ")

testa("N", tabela, (("TB11", "TB12longa", "TB13"), ("TB21", "TB22", "TB23")))

testa("F", cabecalho, "TESTE", False)
testa("T", cabecalho, "TESTE", True)

testa("N", rodape)

testa("T", menu_geral, True, unome, True)
testa("F", menu_geral, True, unome, False)

testa("N", bloco_de_erro, "Você errou, meu amigo!")

testa("N-F", bloco_de_produto, cpr1_ident, prod1, None, False)
testa("N-T", bloco_de_produto, cpr1_ident, prod1, None, True)
testa("10-F", bloco_de_produto, cpr1_ident, prod1, 10, False)
testa("10-T", bloco_de_produto, cpr1_ident, prod1, 10, True)

testa("N", bloco_de_lista_de_produtos, [prod1_ident,prod5_ident,prod2_ident])

testa("F", bloco_de_compra, cpr1, False)
testa("T", bloco_de_compra, cpr1, True)
