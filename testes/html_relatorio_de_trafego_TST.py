import sys

import base_sql
import html_relatorio_de_trafego
import trecho
import sessao
import tabelas
import utils_testes

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = html_relatorio_de_trafego
    funcao = modulo.gera
    frag = True     # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Identificadores de trechos a serem testados para aeroportos VCP e SDU
# trechos_ids_saida_VCP = ["T-00000001", "T-00000007", "T-00000010"]
# trechos_ids_chegada_VCP = ["T-00000002", "T-00000003", "T-00000008", "T-00000011"]
# trechos_ids_saida_SDU = ["T-00000002", "T-00000003", "T-00000004", "T-00000006"]
# trechos_ids_chegada_SDU = ["T-00000001"]

# Gera resumo
resumo_saida_VCP = ("5", "500", "450", "4500", "400")
resumo_chegada_VCP = ("3", "300", "350", "3500", "300")
resumo_saida_SDU = ("6", "600", "650", "6500", "600")
resumo_chegada_SDU = ("1", "100", "50", "500", "25")

testa("VPC_SDU", [("VCP", resumo_chegada_VCP, resumo_saida_VCP), ("SDU", resumo_chegada_SDU, resumo_saida_SDU)])
