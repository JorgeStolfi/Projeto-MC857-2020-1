#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.


import html_form_dados_de_usuario
import html_botao_submit
import usuario
import identificador
import base_sql
import tabelas
import utils_testes

import sys


def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_form_dados_de_usuario
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


# fixtures
sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

# Testes das funções de {gera_html_form}:
usr1 = usuario.busca_por_identificador("U-00000001")
assert usr1 != None
id_usr1 = usuario.obtem_identificador(usr1)
atrs_usr1 = usuario.obtem_atributos(usr1)
assert not usuario.obtem_atributo(usr1, 'administrador')

usr3 = usuario.busca_por_identificador("U-00000003")
assert usr3 != None
id_usr3 = usuario.obtem_identificador(usr3)
atrs_usr3 = usuario.obtem_atributos(usr3)
assert usuario.obtem_atributo(usr3, 'administrador')

atrs_usr0 = atrs_usr1;
del atrs_usr0['nome']
del atrs_usr0['telefone']

ht_bt_coisar = html_botao_submit.gera("Coisar", "coisar", { 'coisa': "568" }, "#ffaa00")

testa("admF_usrN", None,    atrs_usr0, False, ht_bt_coisar)
testa("admF_usrC", id_usr1, atrs_usr1, False, ht_bt_coisar)
testa("admT_usrC", id_usr1, atrs_usr1, True,  ht_bt_coisar)
testa("admT_usrA", id_usr3, atrs_usr3, True,  ht_bt_coisar)
