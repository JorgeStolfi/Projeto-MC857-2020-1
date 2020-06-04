#! /usr/bin/python3

import html_resumo_de_compra
import base_sql
import tabelas
import usuario
import sessao
import compra

import utils_testes

utils_testes.mostra(0, "Conectando com base de dados...")
res = base_sql.conecta("DB",None,None)
assert res == None

utils_testes.mostra(0, "Criando alguns objetos...")
tabelas.cria_todos_os_testes()

# Compras teste
lista_ids = ["C-00000001", "C-00000002", "C-00000003"]

def testa(rotulo, *args):
  modulo = html_resumo_de_compra
  funcao = modulo.gera

  # Teste da função {gera} HTML
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

utils_testes.mostra(0, "Realizando testes com html_resumo_de_compra...")
for id_compra in lista_ids:
  cpr = compra.busca_por_identificador(id_compra)
  assert cpr != None
  testa(id_compra, cpr, False)
  testa(''.join([id_compra, "_V"]), cpr, True)

utils_testes.mostra(2, "Testes realizados com sucesso!")