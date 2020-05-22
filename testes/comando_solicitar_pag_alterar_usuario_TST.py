#! /usr/bin/python3

import comando_solicitar_pag_alterar_usuario
import base_sql
import tabelas
import usuario
import sessao
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Sessão usada no teste
sessao1 = sessao.busca_por_identificador("S-00000001")
assert sessao1 != None

# Usuário usado no teste
usuario1 = usuario.busca_por_identificador("U-00000001")
assert usuario1 != None

def testa(rotulo, *args):
    """Testa {comando_solicitar_pag_alterar_usuario.processa(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_solicitar_pag_alterar_usuario
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa("Sucesso", sessao1, usuario1)
testa("Error", None, None)
