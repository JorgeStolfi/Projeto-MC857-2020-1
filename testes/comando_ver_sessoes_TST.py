import sys
import comando_ver_sessoes
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
tabelas.cria_todos_os_testes()


def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_ver_sessoes
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


# Sessões de teste
ses3 = sessao.busca_por_identificador("S-00000003")

testa("s3",ses3, {'id': 'U-00000001'} )