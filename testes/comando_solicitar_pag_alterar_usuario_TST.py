#! /usr/bin/python3

import comando_solicitar_pag_alterar_usuario
import base_sql
import tabelas
import usuario
import sessao
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

def testa(rotulo, *args):
    """Testa {comando_solicitar_pag_alterar_usuario.processa(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_solicitar_pag_alterar_usuario
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Sessão de cliente comum:
ses1 = sessao.busca_por_identificador("S-00000001")
assert ses1 != None
usr_ses1 = sessao.obtem_usuario(ses1)
assert not usuario.obtem_atributo(usr_ses1, 'administrador')

# Sessão de administrador:
ses4 = sessao.busca_por_identificador("S-00000004")
assert ses4 != None
usr_ses4 = sessao.obtem_usuario(ses4)
assert usuario.obtem_atributo(usr_ses4, 'administrador')

# Usuário comum alterando seus dados:
usr1 = usr_ses1
id_usr1 = usuario.obtem_identificador(usr1)
args_usr1 = { 'id_usuario': id_usr1 }

testa("sesC_usrC", ses1, args_usr1)

# Administrador alterando dados de outro usuário:
testa("sesA_usrC", ses4, args_usr1)
