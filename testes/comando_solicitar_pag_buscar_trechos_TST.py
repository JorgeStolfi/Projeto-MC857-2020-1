import comando_solicitar_pag_buscar_trechos
import utils_testes
import base_sql
import tabelas
import usuario
import sessao
import utils_testes

import sys

sys.stderr.write("Conectando com a base de dados...\n")
res = base_sql.conecta("DB", None, None)

assert res == None  # Verifica que a conexão teve sucesso

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Sessão usada no teste
sessao1 = sessao.busca_por_identificador("S-00000001")
assert sessao1 != None

# Usuário usado no teste
usuario1 = usuario.busca_por_identificador("U-00000001")
assert usuario1 != None

def testa(rotulo, *args):
    """
    Testa se {comando_solicitar_pag_buscar_trecho} retorna  o esperado
    """
    modulo = comando_solicitar_pag_buscar_trecho
    funcao = modulo.processa
    frag = False
    pretty = True
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa("Erro - Não logado", None, None)
testa("Sucesso", sessao1, None)