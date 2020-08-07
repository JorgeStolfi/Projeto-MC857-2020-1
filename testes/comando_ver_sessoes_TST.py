#! /usr/bin/python3
import sys
import comando_ver_sessoes
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

# Sessão de usuário cliente

# Sessão de usuário administrador
ses4 = sessao.busca_por_identificador("S-00000003")

# Usuário a examinar: 

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_ver_sessoes
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Sessão de cliente comum:
ses1 = sessao.busca_por_identificador("S-00000002")
assert not sessao.eh_administrador(ses1)
usr1 = sessao.obtem_usuario(ses1)
usr1_id = usuario.obtem_identificador(usr1)
testa("teste1-N", ses1, {} )  
testa("teste1-U", ses1, {'id': usr1_id } )  

# Administrador olhando suas sessões:
ses2 = sessao.busca_por_identificador("S-00000004")
assert sessao.eh_administrador(ses2)
usr2_id = "U-00000002"
testa("teste2-N", ses2, {} )  
testa("teste2-U", ses2, {'id': usr2_id } )  

