import sys

import base_sql
import comando_solicitar_pag_clonar_trecho
import sessao
import tabelas
import trecho
import utils_testes

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

def testa(rotulo, *args):
    """Testa {comando_solicitar_pag_clonar_trecho.processa(ses, *args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_solicitar_pag_clonar_trecho
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


# sessão usada no teste
sessao1 = sessao.busca_por_identificador("S-00000001")
assert sessao1 != None

# Testa duas vezes: com uma sessão válida e também com uma sessão inválida (nula), para testar
# o comportamento do módulo em diferentes cenários, garantindo sua funcionalidade.
testa("teste_clonar_trecho_sessao_valida", sessao1, {"id_trecho": "T-00000001"})
testa("teste_clonar_trecho_sessao_nula", None, {"id_trecho": "T-00000001"})
