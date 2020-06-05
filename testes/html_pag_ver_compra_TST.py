#! /usr/bin/python3

import html_pag_ver_compra
import base_sql
import utils_testes
import compra
import tabelas
import sessao
import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Sessão que será utilizada no teste
ses = sessao.busca_por_identificador("S-00000001")

# Compra que será utilizada no teste
cpr = compra.busca_por_identificador("C-00000001")


def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = html_pag_ver_compra
    funcao = modulo.gera
    frag = False # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Testa com e sem a opção de excluir habilitada
testa("xT-E0", ses, cpr, True,  None)
testa("xT-E1", ses, cpr, True,  "Tem algo de podre no Reino de Dinamarca")
testa("xF-E0", ses, cpr, False, None)
