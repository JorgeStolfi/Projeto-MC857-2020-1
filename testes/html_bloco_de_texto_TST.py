#! /usr/bin/python3

import html_bloco_texto
from utils_testes import testa_modulo_html
import sys

def cria_linha(disp):
  """Cria uma linha de teste com {disp} dado."""
  t1 = html_bloco_texto.gera(disp, "Hello C","Helvetica","18px","bold","30px","center","#000000","#ff8800")
  t2 = html_bloco_texto.gera(disp, "Hello L","Courier","18px",None,"0px","left","#000000","#8844ff")
  t3 = html_bloco_texto.gera(disp, "Hello R","Courier","12px",None,"1px","right","#000000","#8844ff")
  linha = "<li> disp = " + disp + ": " + \
    "Lorem ipsum" + t1 + \
    "Gallia omnia" + t2 + \
    "Quousque tandem" + t3 + \
    "Pluribus unum" + \
    "</li>"
  return linha

def cria_pagina():
  linha1 = cria_linha("inline_block")
  linha2 = cria_linha("block")
  pagina = "<ul>\n" + \
    linha1 + "\n" + \
    linha2 + "\n" + \
    "</ul>"
  return pagina

pag = cria_pagina()
testa_modulo_html(html_bloco_texto, "diversos", pag, True, False)
