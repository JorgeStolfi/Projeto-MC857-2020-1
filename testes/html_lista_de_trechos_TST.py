import sys

import base_sql
import html_lista_de_trechos
import tabelas
import utils_testes
import trecho

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()


def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = html_lista_de_trechos
    funcao = modulo.gera
    frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


trc1_id = "T-00000001"
trc2_id = "T-00000002"
trc3_id = "T-00000003"
trc4_id = "T-00000004"
trc5_id = "T-00000005"
trc6_id = "T-00000006"

trechos_ids = [ trc1_id, trc2_id, trc3_id, trc4_id, trc5_id, trc6_id ]
trechos_list = map(lambda x: trecho.busca_por_identificador(x), trechos_ids)

testa("altF", None, trechos_ids, False)
testa("altT", None, trechos_ids, True)
