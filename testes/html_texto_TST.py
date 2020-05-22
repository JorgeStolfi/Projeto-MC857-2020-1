#! /usr/bin/python3

import html_texto
from utils_testes import testa_modulo_html
import sys

def cria_linha(disp):
  """Cria uma linha de teste com {disp} dado."""
  t1 = html_texto.gera(disp, disp,"Helvetica","18px","normal","30px","center","#ffffff","#8844ff")
  t2 = html_texto.gera(disp, disp,"Courier","15px","normal","0px","left","#000000","#4C61FF")
  t3 = html_texto.gera(disp, disp,"Courier","12px","900","5px","right","#000000","#E135FF")
  linha = "<li> disp = " + disp + ": " + \
    "Lorem ipsum" + t1 + \
    "Gallia omnia" + t2 + \
    "Quousque tandem" + t3 + \
    "Pluribus unum" + \
    "</li>"
  return linha

def cria_pagina():
  linha1 = cria_linha("inline-block")
  linha2 = cria_linha("block")
  pagina = "<ul>\n" + \
    linha1 + "\n" + \
    linha2 + "\n" + \
    "</ul>"
  return pagina

pag = cria_pagina()
testa_modulo_html(html_texto, "diversos", pag, True, False)
