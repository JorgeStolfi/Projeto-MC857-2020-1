#! /usr/bin/python3

import base_sql
import tabelas
import sessao
import utils_testes
import comando_sugerir_roteiros

import sys


sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_sugerir_roteiros
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

ses1 = sessao.busca_por_identificador("S-00000001")
assert ses1 != None

dados = {
    "origem": "VCP",
    "destino": "MAO",
    "dia_min": "2020-01-01",
    "dia_max": "2020-12-31"
}
testa("sucesso-sugerir-roteiros", ses1, dados)
