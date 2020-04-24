#! /usr/bin/python3

import html_menu_geral; from html_menu_geral import gera
import utils_testes; from utils_testes import testa_gera_html as testa

testa(html_menu_geral, gera, "deslogado", True, False,   False, None,            False)
testa(html_menu_geral, gera, "cliente",   True, False,   True,  "José Primeiro", False)
testa(html_menu_geral, gera, "admin",     True, False,   True,  "Geraldo Ente",  True)

