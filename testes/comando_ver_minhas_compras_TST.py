#! /usr/bin/python3

import sys
import comando_ver_minhas_compras
import base_sql
import tabelas
import usuario
import sessao
import compra
import utils_testes

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando objetos...\n")
tabelas.cria_todos_os_testes(False)

# Sessões de teste
ses_nao_admin = sessao.busca_por_identificador("S-00000001")
admin = usuario.busca_por_identificador("U-00000003")
ses_admin = sessao.cria(admin, "NOPQRSTUVWX", None)

args = None

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_ver_minhas_compras
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa("Logado", ses_nao_admin, args)
testa("Administrador", ses_admin, args)
# testa("Anonimo", None, args)

