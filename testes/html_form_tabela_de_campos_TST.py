#! /usr/bin/python3

import html_form_tabela_de_campos
import base_sql
import identificador
import sessao
import tabelas
import usuario
import utils_testes

import sys

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_form_tabela_de_campos
  funcao = modulo.gera
  frag = False # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

dados_linhas = [("Nome", "text", "entradaNome", "", True),
                ("Idade", "number", "entradaIdade", "XX", True),
                ("Telefone", "tel", "entradaTel", "+XX (XX) XXXXX-XXXX", False),
                ("Email", "email", "entradaEmail", "email@domain.com", False),
                ("Administrador", "checkbox", "checkboxAdmin", "", True)]

atrs = {"entradaNome":"João Pedro II",
        "entradaIdade":22,
        "entradaTel":"+55 (19) 12345-6789",
        "entradaEmail":"joaopedroii@email.com",
        "checkboxAdmin":True}

testa("html_form_tabela_campos_user", dados_linhas, atrs, False)
testa("html_form_tabela_campos_admin", dados_linhas, atrs, True)

