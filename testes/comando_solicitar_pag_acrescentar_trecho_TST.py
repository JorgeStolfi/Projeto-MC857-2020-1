import sys

import base_sql
import comando_solicitar_pag_acrescentar_trecho
import sessao
import tabelas
import utils_testes

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

def testa(rotulo, *args):
    """Testa {comando_solicitar_pag_alterar_usuario.processa(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_solicitar_pag_acrescentar_trecho
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


# sessão usada no teste
ses1 = sessao.busca_por_identificador("S-00000004")
assert ses1 != None
assert sessao.eh_administrador(ses1)

testa("teste_acrescentar_trecho_sessao_valida", ses1, {})

