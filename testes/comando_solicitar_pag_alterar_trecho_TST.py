#! /usr/bin/python3

import comando_solicitar_pag_alterar_trecho
import base_sql
import tabelas
import trecho
import sessao
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

def testa(rotulo, *args):
    """Testa {comando_solicitar_pag_alterar_trecho.processa(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_solicitar_pag_alterar_trecho
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# sessão usada no teste
ses1 = sessao.busca_por_identificador("S-00000004")
assert ses1 != None
assert sessao.eh_administrador(ses1)

args1['id_trecho'] = "T-00000001"
# Teste mostra os dados do dono do identificador passado
testa("S-comID", ses1, args1)
