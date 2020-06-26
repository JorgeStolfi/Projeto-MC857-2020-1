#! /usr/bin/python3

import sys
import comando_trocar_poltrona
import base_sql
import tabelas
import sessao
import compra
import poltrona
import trecho
from utils_testes import erro_prog, testa_gera_html

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando objetos...\n")
tabelas.cria_todos_os_testes()
def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_trocar_poltrona
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

ses = sessao.busca_por_identificador("S-00000003")
trc = trecho.busca_por_identificador("T-00000003")

testa("A1-T3-C3", ses, "A-00000008", trc, "C-00000003")
