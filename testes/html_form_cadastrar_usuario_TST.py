#! /usr/bin/python3

import html_form_cadastrar_usuario
import usuario
import identificador
import base_sql
import tabelas
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Testes das funções de {gera_html_form}:

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_form_cadastrar_usuario
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


# Teste01: {atrs} = {None} e {admin} = {True}
atr = None
admin = True

testa("Vazio_Admin", atr, admin)

# Teste02: {atrs} = {None} e {admin} = {False}
atr = None
admin = False

testa("Vazio_Comum", atr, admin)

# Teste03: {atrs} = valores e {admin} = {True}
atr = {'nome':'usario teste',
       'senha':'1234567890',
       'email':'test@email.com',
       'CPF':'123.456.789-00',
       'telefone':'+55(19)9999-9999',
       'documento':'12.123.123-1'}
admin = True

testa("Valores_Admin", atr, admin)

# Teste04: {atrs} = valores e {admin} = {False}
atr = {'nome':'usario teste',
       'senha':'1234567890',
       'email':'test@email.com',
       'CPF':'123.456.789-00',
       'telefone':'+55(19)9999-9999',
       'documento':'12.123.123-1'}
admin = False

testa("Valores_Comum", atr, admin)

# Teste05: {atrs} = valores menos a senha e {admin} = {True}
atr = {'nome':'usario teste',
       'email':'test@email.com',
       'CPF':'123.456.789-00',
       'telefone':'+55(19)9999-9999',
       'documento':'12.123.123-1'}
admin = True

testa("Sem_Senha_Admin", atr, admin)

# Teste06: {atrs} = valores menos a senha e {admin} = {False}
atr = {'nome':'usario teste',
       'email':'test@email.com',
       'CPF':'123.456.789-00',
       'telefone':'+55(19)9999-9999',
       'documento':'12.123.123-1'}
admin = False

testa("Sem_Senha_Comum", atr, admin)

# Teste07: {atrs} = somente o nome e {admin} = {True}
atr = {'nome':'usario teste'}
admin = True

testa("Nome_Admin", atr, admin)

# Teste08: {atrs} = somente o nome e {admin} = {False}
atr = {'nome':'usario teste'}
admin = False

testa("Nome_Admin", atr, admin)
