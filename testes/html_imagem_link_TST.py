#! /usr/bin/python3

import html_imagem_link
import utils_testes

def testa(rotulo, *args):
  """Testa {funcao(*args, "elucubrar")}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = html_imagem_link
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, modulo.gera, rotulo, frag, pretty, *args)


testa("img1", "/13802.jpg", "13802", 100, "urlteste")

testa("img2", "/AZ.png", "AZ", 50, "urlteste")

testa("img3", "/GO.png", "GO", 75, "urlteste")

testa("imgFalsa", "/falsa.png", "falsa", 150, "urlteste")

testa("noImg", NULL, "no image", 150, "urlteste")
