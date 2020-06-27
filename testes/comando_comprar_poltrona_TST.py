import sys
import comando_comprar_poltrona
import base_sql
import tabelas
import usuario
import sessao
import compra
import utils_testes 

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando objetos...\n")
tabelas.cria_todos_os_testes()

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_comprar_poltrona
    funcao = modulo.processa
    frag = False
    pretty = True
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

ses = sessao.busca_por_identificador("S-00000001")
assert ses != None

testa("comprar poltrona", ses, None)
