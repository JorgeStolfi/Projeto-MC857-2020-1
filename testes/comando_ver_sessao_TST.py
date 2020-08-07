#! /usr/bin/python3
import sys
import comando_ver_sessao
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

# Usuário a examinar: 

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_ver_sessao
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


id_ses = "S-00000001"
ses1 = sessao.busca_por_identificador(id_ses)

# Sessão de cliente comum:
testa("uso_comum", ses1, {'id_sessao': 'S-00000001'})  

# Cliente tentando acessar sessão que não e dele:
testa("acesso_invalido", ses1, {'id_sessao': 'S-00000003'})  

# Chamada sem argumentos
testa("sem_argumento", ses1, {})  


