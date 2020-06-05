#! /usr/bin/python3

# Interfaces usadas por este script:

import html_form
import html_label
import html_input
import html_table
import html_botao_submit
from utils_testes import testa_modulo_html

import sys

def cria_form_completo():
  linhas = [].copy()
  
  # cria campo de teste comum
  ht_rotulo = html_label.gera("campo de texto", ": ")
  ht_campo = html_input.gera(None, "text", "texto", None, True, None, None)
  linhas.append((ht_rotulo, ht_campo,))

  # cria campo de senha
  ht_rotulo = html_label.gera("campo de senha", ": ")
  ht_campo = html_input.gera(None, "password", "senha", None, True, None, None)
  linhas.append((ht_rotulo, ht_campo,))

  # cria campo numerico
  ht_rotulo = html_label.gera("campo numerico", ": ")
  ht_campo = html_input.gera(None, "number", "numero", None, True, None, None)
  linhas.append((ht_rotulo, ht_campo,))

  # cria campo escondido
  ht_rotulo = html_label.gera("campo escondido", ": ")
  ht_campo = html_input.gera(None, "hidden", "hidden", None, True, None, None)
  linhas.append((ht_rotulo, ht_campo,))

  # Monta a tabela com os fragmentos HTML:
  ht_table = html_table.gera(linhas)

  # cria botao de interacao com o formulario
  ht_botao = html_botao_submit.gera("Botao", 'url test', None, '#55ee55')

  # counteudo do formulario
  ht_campos = \
    ht_table + \
    ht_botao

  # cria formulario de teste
  formulario = html_form.gera(ht_campos)
  return formulario

form_completo = cria_form_completo()
testa_modulo_html(html_form, "completo", form_completo, True, False)
