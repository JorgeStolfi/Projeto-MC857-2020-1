#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import html_form
import usuario
import identificador
import base_sql
import tabelas
import sessao
#import produto
import compra
import utils_testes
import comando_alterar_usuario

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Testes das funções de {html_form}:

def testa(rotulo,  funcao, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/html_form.{rotulo}.html"."""
  
  modulo = html_form
  frag = True
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, *args) # parei aqui

ses = sessao.busca_por_identificador("S-00000001")
assert ses != None
assert sessao.aberta(ses)

usr1 = sessao.obtem_usuario(ses)
assert usr1 != None

prod1_ident = "P-00000001"
#prod1 = produto.busca_por_identificador(prod1_ident)
#assert prod1 != None

prod2_ident = "P-00000002"
#prod2 = produto.busca_por_identificador(prod2_ident)
#assert prod2 != None

cpr1_ident = "C-00000001"
cpr1 = compra.busca_por_identificador(cpr1_ident)
assert cpr1 != None

#testa("buscar_produtos", buscar_produtos)

#testa("ver_produto", ver_produto, prod1_ident, 3)

#testa("comprar_produto", comprar_produto, cpr1_ident, prod1_ident, 3)

#testa("alterar_quantidade", alterar_quantidade, cpr1_ident, prod1_ident, 5)

# Nao implementadas em gera_html_botao
#testa("ver_compra", ver_compra, cpr1_ident)

# Nao implementada em gera_html_botao
#testa("fechar_compra", fechar_compra, cpr1_ident)

# testa("entrar", entrar)