#! /usr/bin/env python3

import html_pag_alterar_trecho
import tabelas
import usuario
import sessao
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
    ("S-00000001", "U1-S01", "Erro 1: Não era pra você estar aqui!"), 
    ("S-00000004", "U3-S04", "Erro 2: A função ainda não foi implementada!")  # Usuário com privilégio
  ):
  ses = sessao.busca_por_identificador(ses_id)
  assert ses != None

  usr = sessao.obtem_usuario(ses)
  assert usr != None
  usr_id = usuario.obtem_identificador(usr)

  rotulo = tag + "_" + erros
  testa(rotulo, ses, usr_id, trc1_id, {}, erros)
