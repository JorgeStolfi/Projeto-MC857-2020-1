import sys
import comando_fechar_sessao
import base_sql
import tabelas
import sessao
import utils_testes

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando objetos...\n")
tabelas.cria_todos_os_testes()

ses = sessao.busca_por_identificador("S-00000001")

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
    modulo = comando_fechar_sessao
    funcao = modulo.processa
    frag = False
    pretty = False
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

ses = sessao.busca_por_identificador("S-00000001")
assert ses != None
assert sessao.aberta(ses)

for rotulo, sessao, args in [   #('Sessão inexistente',          ses,    {'id_sessao' : ''}) Não está implementado um tratamento para sessão inexistente
                                ('Sessão existente',            ses,    {'id_sessao' : 'S-00000002'}),
                                ('Sessão do próprio usuário',   ses,    {'id_sessao' : 'S-00000001'}),
                                ('Sessão atual fechada',        ses,    {'id_sessao' : 'S-00000003'})
                            ]:

    testa(rotulo, sessao, args)
