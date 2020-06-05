#! /usr/bin/python3

import comando_solicitar_pag_buscar_compras
import tabelas
import sessao
import base_sql
import utils_testes

import sys

# Conecta no banco e alimenta com as informações para o teste


sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Sessão de teste
ses = sessao.busca_por_identificador("S-00000001")

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = comando_solicitar_pag_buscar_compras
  funcao = modulo.processa
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


testa("retorna-pagina-busca", ses, None)
