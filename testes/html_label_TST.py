#! /usr/bin/python3

import html_label 
import utils_testes
import sys

modulo = html_label
funcao = modulo.gera
frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
utils_testes.testa_gera_html(modulo, funcao, "1", frag, pretty, "Banana", " --> ")
