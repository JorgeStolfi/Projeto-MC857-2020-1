#! /usr/bin/python3

# Interfaces usadas por este script:

import base_sql
import tabelas
import usuario
import produto
import sessao
import compra
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Testes das funções de {html_bloco_de_erro}:

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/html_{modulo}.{rotulo}.html"."""
  
  modulo = html_bloco_de_erro
  frag = True
  utils_testes.testa_gera_html(modulo, modulo.gera, rotulo, frag, *args)

ses = sessao.busca_por_identificador("S-00000001")
assert ses != None
assert sessao.aberta(ses)

usr = sessao.obtem_usuario(ses)
assert usr != None
unome = usuario.obtem_atributos(usr)['nome']

prod1_ident = "P-00000001"
prod1 = produto.busca_por_identificador(prod1_ident)
prod2_ident = "P-00000002"
prod5_ident = "P-00000005"

cpr1_ident = "C-00000001"
cpr1 = compra.busca_por_identificador(cpr1_ident)

testa("N", "Você errou, meu amigo!")
