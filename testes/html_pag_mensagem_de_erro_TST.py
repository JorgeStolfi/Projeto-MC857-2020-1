#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# retornam cadeias de caracteres que são 
# páginas completas em HTML5

# !!! Fazer este programa de teste funcionar !!!
# !!! Ele ptecisa chamar cada função da interface pelo menos uma vez, gravando arquivos ".html" separados. !!!

#Interfaces utilizados por este teste

import tabelas
import usuario
import produto
import compra
import sessao
import html_pag_generica
import base_sql
from produto import ObjProduto
import utils_testes

import sys

# Cria alguns produtos:

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()
#usuario teste
usr1_id = usuario.busca_por_CPF("123.456.789-00")
usr1 = usuario.busca_por_identificador(usr1_id)
usr1_atrs = usuario.obtem_atributos(usr1)

#sessao de teste
ses = sessao.busca_por_identificador("S-00000001")

#carrinho de teste

carr = sessao.obtem_carrinho(ses)
cpr_ident = "C-00000003"
cpr = compra.busca_por_identificador(cpr_ident)

#qtd teste
qtd = 2.3
#produto teste
prod1 = produto.busca_por_identificador("P-00000001")
lista_prod = ["P-00000001", "P-00000002"]

# Testes das funções de {html_pag_generica}:

def testa(nome, tag, funcao, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/html_pag_generica.{nome}_{tag}.html"."""
  
  modulo = html_pag_generica
  frag = False
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, *args)
  
# !!! Completar !!!

msg = "voce cometeu um erro, rapaz"
testa("mensagem_de_erro", "S", html_pag_generica.mensagem_de_erro, ses, msg)

msg = "voce cometeu um erro, rapaz\ne outro erro também"
testa("mensagem_de_erro", "M", html_pag_generica.mensagem_de_erro, ses, msg)

msg = ["voce cometeu um erro, rapaz", "e outro erro também",]
testa("mensagem_de_erro", "L", html_pag_generica.mensagem_de_erro, ses, msg)

for tag, erros in ( 
    ("N", None), 
    ("V", []), 
    ("E", ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",])
  ):

  testa("principal", tag, html_pag_generica.principal, ses, erros)

  testa("produto", tag, html_pag_generica.mostra_produto, ses, cpr_ident, prod1, qtd, erros)

  testa("lista_de_produtos", tag, html_pag_generica.lista_de_produtos, ses, lista_prod, erros)

  testa("cadastrar_usuario", tag, html_pag_generica.cadastrar_usuario, ses, usr1_atrs,["erro 1", "erro 2",])

  testa("alterar_usuario", tag, html_pag_generica.alterar_usuario, ses, usr1_id, usr1_atrs, ["erro bobo", "erro genial",])

  conteudo = "Teste do método genérico"

  testa("generica", tag, html_pag_generica.generica,ses, conteudo, erros)

  testa("mostra_carrinho", tag, html_pag_generica.mostra_carrinho, ses, erros)

  testa("mostra_compra_False", tag, html_pag_generica.mostra_compra, ses, cpr, erros)
  testa("mostra_compra_True", tag, html_pag_generica.mostra_compra, ses, cpr, erros)







