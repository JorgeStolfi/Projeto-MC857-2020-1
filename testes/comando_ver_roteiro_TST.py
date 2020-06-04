#! /usr/bin/python3

#! /usr/bin/python3

import comando_ver_roteiro
import tabelas
import sessao
import usuario
import base_sql
import utils_testes

import sys

# Conecta no banco e alimenta com as informações para o teste
sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Sessões de teste
ses_nao_admin = sessao.busca_por_identificador("S-00000001")
admin = usuario.busca_por_identificador("U-00000003")
ses_admin = sessao.cria(admin, "NOPQRSTUVWX", None)

args_trechos = {
  'ids_trechos': 'T-00000001,T-00000003,T-00000005'
}
args_trecho_unico = {
  'ids_trechos': 'T-00000003'
}
def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_ver_roteiro
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Teste para mais de um trecho
testa("Logado-trechos", ses_nao_admin, args_trechos)
testa("Administrador-trechos", ses_admin, args_trechos)
testa("Anonimo-trechos", None, args_trechos)

# Teste para só um trecho
testa("Logado-trecho-unico", ses_nao_admin, args_trecho_unico)
testa("Administrador-trecho-unico", ses_admin, args_trecho_unico)
testa("Anonimo-trecho-unico", None, args_trecho_unico)

# Teste para dicionario vazio (sem a chave)
testa("Logado-vazio", ses_nao_admin, {})
testa("Administrador-vazio", ses_admin, {})
testa("Anonimo-vazio", None, {})

# Teste para dicionario nulo
testa("Logado-nulo", ses_nao_admin, None)
testa("Administrador-nulo", ses_admin, None)
testa("Anonimo-nulo", None, None)