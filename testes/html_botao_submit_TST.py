#! /usr/bin/python3

import html_botao_submit
from html_botao_submit import gera

from utils_testes import testa_gera_html as testa
import sys

testa(html_botao_submit, gera, "submit_Cadastrar", True, False, "Cadastrar", 'cadastrar_usuario', None, '#55ee55')

testa(html_botao_submit, gera, "submit_Alterar_usuario", True, False, "Alterar", 'alterar_usuario', {'id_usuario': "U-00000001"}, '#55ee55')

testa(html_botao_submit, gera, "submit_Entrar", True, False, "Entrar", 'fazer_login', None, '#55ee55')
