#! /usr/bin/python3

import html_estilo_de_botao
from html_estilo_de_botao import gera

from utils_testes import testa_gera_html as testa
import sys

testa(html_estilo_de_botao, gera, "estilo_de_botao_1", True, False, '#60a3bc')
