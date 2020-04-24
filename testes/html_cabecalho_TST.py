#! /usr/bin/python3

import html_cabecalho; from html_cabecalho import gera
import utils_testes; from utils_testes import testa_gera_html as testa

testa(html_cabecalho, gera, "P", True, False, "TESTINHO", False)
testa(html_cabecalho, gera, "G", True, False, "TESTÃO", True)
