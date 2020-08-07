
import sys
import comando_definir_carrinho
import base_sql
import tabelas
import usuario
import sessao
import compra
import utils_testes

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

id_compra = "C-00000001"
ses = sessao.busca_por_identificador("S-00000001")
usr = usuario.busca_por_identificador("U-00000001")
compra = compra.busca_por_identificador(id_compra)
assert ses != None
assert compra != None

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
    modulo = comando_definir_carrinho
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


args = { "id_compra": id_compra }
testa("sucesso", ses, args)


