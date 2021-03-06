#! /usr/bin/python3

import comando_alterar_trecho
import tabelas
import trecho
import usuario
import sessao
import base_sql
import utils_testes

import sys

# Conecta no banco e carrega alimenta com as informações para o teste

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

# Sessao de teste
ses = sessao.busca_por_identificador("S-00000001")

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_alterar_trecho
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

def testa_atualiza_atributo_com_sucesso():
   
    args = {
        'id_trecho': "T-00000001",
        'destino': 'POA'
    }

    testa("Suc", ses, args)

    updated_trecho = trecho.busca_por_identificador("T-00000001")

    assert trecho.obtem_atributo(updated_trecho, "destino") == 'POA', "Trecho não atualizado"

# Executa os testes

testa_atualiza_atributo_com_sucesso()
