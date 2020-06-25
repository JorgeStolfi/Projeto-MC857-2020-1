#! /usr/bin/env python3

import html_pag_alterar_trecho
import tabelas
import usuario
import sessao

import trecho
import base_sql
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Trecho de teste (somente id):
trc1_id = "T-00000001"

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_pag_alterar_trecho
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidade (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

for ses_id, tag, erros in ( 
    ("S-00000001", "U1-S01-E0", None), # Usuário comum.
    ("S-00000001", "U1-S01-E1", "Não era pra você estar aqui!"), # Usuário comum.
    ("S-00000004", "U3-S04-E2", [ "Não estou bonzinho hoje", "Não vou com a sua cara"])  # Usuário administrador.
  ):
  rotulo = tag # Rotulo do teste.
  
  trc_id = trc1_id # Trecho a alterar.

  trc = trecho.busca_por_identificador(trc_id)
  trc_args = trecho.obtem_atributos(trc) # Valores iniciais dos campos a mostrar na página.
  
  ses = sessao.busca_por_identificador(ses_id) # Sessão de quem está alterando.
  assert ses != None

  usr = sessao.obtem_usuario(ses) # Usuário que está pedindo a alteração.
  assert usr != None
  usr_id = usuario.obtem_identificador(usr)

  testa(rotulo, ses, trc_id, trc_args, erros)
