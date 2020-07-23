import sys

import base_sql
import html_lista_de_compras
import sessao
import tabelas
import utils_testes

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

cpr1_id = "C-00000001"
cpr2_id = "C-00000002"
cpr3_id = "C-00000003"

compras_ids = [cpr1_id, cpr2_id, cpr3_id]

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = html_lista_de_compras
    funcao = modulo.gera
    frag = True     # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


testa("testa_sem_ver", compras_ids, False, cpr1_id)
testa("testa_com_ver", compras_ids, True, cpr1_id)
