import sys
import comando_comprar_poltrona
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
tabelas.cria_todos_os_testes(False)

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_comprar_poltrona
    funcao = modulo.processa
    frag = False
    pretty = True
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

ses1 = sessao.busca_por_identificador("S-00000001")
assert ses1 != None
cpr1 = sessao.obtem_carrinho(ses1)
cpr1_id = compra.obtem_identificador(cpr1)

pol1_id = "A-00000002" # Deve estar livre.
pol1 = poltrona.busca_por_identificador(pol1_id)
assert poltrona.obtem_atributo(pol1, 'id_compra') == None 
args1 = { 'id_poltrona': pol1_id, }
testa("comprar", ses1, args1)
assert poltrona.obtem_atributo(pol1, 'id_compra') == cpr1_id

