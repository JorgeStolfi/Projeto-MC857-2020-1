import sys
import comando_finalizar_compra   
import html_pag_mensagem_de_erro
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
tabelas.cria_todos_os_testes(False)

id_compra = "C-00000001"
ses = sessao.busca_por_identificador("S-00000001")
usr = usuario.busca_por_identificador("U-00000001")
compra = compra.busca_por_identificador(id_compra)
args = {}

if compra: # Se há compra, coleta dados
    sys.stderr.write("Compra encontrada\n")
    args = { "id_compra": compra.id}
else: # Não há compra com o id proposto
    erro_prog("comando_finalizar_compra_TST : teste falhou : compra nao encontrada")
    # Pagina de erro gerada pelo modulo {comando_ver_compra} caso algo de errado
    erros = ["compra \"" + id_compra + "\" não existe"]
    pag_erro = html_pag_mensagem_de_erro.gera(ses, erros)

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
    modulo = comando_finalizar_compra
    funcao = modulo.processa
    frag = False
    pretty = False
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

ses = sessao.busca_por_identificador("S-00000001")
assert ses != None
assert sessao.aberta(ses)

testa("C", ses, args)
