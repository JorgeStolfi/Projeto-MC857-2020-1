#! /usr/bin/python3

import html_rodape; from html_rodape import gera
import utils_testes; from utils_testes import testa_gera_html as testa

testa(html_rodape, gera, "N", True, False)
