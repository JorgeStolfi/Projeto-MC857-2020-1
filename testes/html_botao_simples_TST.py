#! /usr/bin/python3

import html_botao_simples
from html_botao_simples import gera

from utils_testes import testa_gera_html as testa

testa(html_botao_simples, gera, "simples_Principal", True, False, "Principal", 'principal', None, '#60a3bc')

testa(html_botao_simples, gera, "simples_Entrar", True, False, "Entrar", 'solicitar_form_de_login', None, '#55ee55')

testa(html_botao_simples, gera, "simples_Sair", True, False, "Sair", 'fazer_logout', None, '#60a3bc')

testa(html_botao_simples, gera, "simples_Cadastrar", True, False, "Cadastrar", 'solicitar_form_de_cadastrar_usuario', None, '#60a3bc')

testa(html_botao_simples, gera, "simples_OK", True, False, "OK", 'principal', None, '#55ee55')
