#! /usr/bin/python3

import comando_buscar_trechos
import tabelas
import usuario
import sessao
import base_sql
import utils_testes

import sys

# Conecta no banco e carrega alimenta com as informações para o teste

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Sessao de teste
ses = sessao.busca_por_identificador("S-00000001")


def testa(rotulo, ses, args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = comando_buscar_trechos
  pag = modulo.processa(ses, args)
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_modulo_html(modulo, rotulo, pag, frag, pretty)


testa('Teste nenhum campo informado', ses, {})
testa('Teste campo informado apenas com None', ses, {'origem': None})
testa('Teste buscar trecho', ses, {'origem': 'SDU'})
