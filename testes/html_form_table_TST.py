#! /usr/bin/python3

import html_form_table
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
  
  modulo = html_form_table
  funcao = modulo.gera
  frag = False # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

dados_linhas = [ \
  ( "Nome",          "text",     "nome",    "",                    True,  True,  True,  ),
  ( "Idade",         "number",   "idade",   "NN",                  True,  True,  False, ), # Opcional.
  ( "Pernas",        "number",   "pernas",  None,                  True,  False, True,  ), # Readonly.
  ( "Segredo",       "text",     "segredo", None,                  False, False, True,  ), # Hidden.
  ( "Telefone",      "text",     "tel",     "+XX (XX) XXXXX-XXXX", True,  True,  False, ), # Opcional.
  ( "E-mail",        "email",    "email",   "email@domain.com",    True,  True,  True,  ),
  ( "Administrador", "checkbox", "admin",  "",                     True,  True,  True,  ),
]

atrs = {
  "nome": "João Pedro II",
  "idade": 22,
  "idade_min": 13,
  "pernas": 2,
  "segredo": "gosta de Maria",
  "tel": "+55 (19) 12345-6789",
  "email": "joaopedroii@email.com",
  "admin": True,
}

testa("html_form_table_campos_user", dados_linhas,  atrs)

