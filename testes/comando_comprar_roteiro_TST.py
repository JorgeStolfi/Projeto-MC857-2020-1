import sys
import comando_comprar_roteiro
import base_sql
import tabelas
import usuario
import sessao
import compra
import poltrona
import utils_testes 
from utils_testes import aviso_prog, erro_prog
from valida_campo import ErroAtrib

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando objetos...\n")
tabelas.cria_todos_os_testes()

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_comprar_roteiro
    funcao = modulo.processa
    frag = False
    pretty = True
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

ses1 = sessao.busca_por_identificador("S-00000001")
assert ses1 != None

roteiro = ["T-00000003", "T-00000004"]
args = {'ids_trechos': roteiro}
testa("comprar_roteiro_usr_logado", ses1, args)

ses2 = sessao.busca_por_identificador("S-00000002")
assert ses2 != None

testa("comprar_roteiro_lotado", ses2, args)

ses3 = None
testa("comprar_roteiro_deslogado", ses3, args)

