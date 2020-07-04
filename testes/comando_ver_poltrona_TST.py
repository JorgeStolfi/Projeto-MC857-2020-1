import sys
import base_sql
import sessao
import tabelas
import utils_testes
import comando_ver_poltrona

# Conecta no banco e carrega alimenta com as informações para o teste
sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("../DB", None, None)
assert res is None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

def testa(rotulo, *args):
    """Testa {comando_solicitar_pag_alterar_usuario.processa(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_ver_poltrona
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Sessão utilizada para testes
ses = sessao.busca_por_identificador("S-00000001")

# Poltrona válida utilizada para testes
args_pol_valida = {'id_poltrona': 'A-00000001'}

# Poltrona inexistente utilizada para testes
args_pol_inexistente = {'id_poltrona': 'A-00000000'}

# Teste com uma poltrona válida. Deve retornar uma página html com as informações da poltrona.
testa("Teste com poltrona válida", ses, args_pol_valida)

# Teste com uma poltrona inexistente. Deve retornar uma página html com erro.
testa("Teste com poltrona inexistente", ses, args_pol_inexistente)

# Testa com uma sessão inexistente. Deve retornar uma página html com erro.
testa("Teste com sessão inexistente", None, args_pol_valida)


