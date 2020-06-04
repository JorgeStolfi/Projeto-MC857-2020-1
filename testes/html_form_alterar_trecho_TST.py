#! /usr/bin/python3

import html_form_alterar_trecho
import trecho
import base_sql
import tabelas
import sys
import utils_testes 

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

def testa(rotulo, *args):

  modulo = html_form_alterar_trecho
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)
  
trc1 = trecho.busca_por_identificador("T-00000001")
assert trc1 != None
atributosTrc1 = trecho.obtem_atributos(trc1)
testa("TESTE_TRECHO_1", "T-00000001", atributosTrc1)

trc2 = trecho.busca_por_identificador("T-00000002")
assert trc2 != None
atributosTrc2 = trecho.obtem_atributos(trc2)
testa("TESTE_TRECHO_2", "T-00000002", atributosTrc2)

trc3 = trecho.busca_por_identificador("T-00000003")
assert trc3 != None
atributosTrc3 = trecho.obtem_atributos(trc3)
testa("TESTE_TRECHO_3", "T-00000003", atributosTrc3)
