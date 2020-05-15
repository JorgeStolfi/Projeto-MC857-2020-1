#! /usr/bin/python3

import comando_alterar_usuario
import tabelas
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
tabelas.cria_todos_os_testes()

# Sessao de teste
ses = sessao.busca_por_identificador("S-00000001")


def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_alterar_usuario
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


def testa_atualiza_atributo_com_sucesso():
    novo_nome = "John First"
    args = {
        'id_usuario': "U-00000001",
        'nome': novo_nome,
    }
    testa("Suc", ses, args)

    updated_user = usuario.busca_por_identificador("U-00000001")

    assert usuario.obtem_atributo(updated_user, "nome") == novo_nome, "Nome não atualizado"


def testa_atualiza_atributo_invalido():
    cpf_invalido = "123.123.123"
    args = {
        'id_usuario': "U-00000001",
        'CPF': cpf_invalido,
    }
    testa("Inv", ses, args)

    updated_user = usuario.busca_por_identificador("U-00000001")

    assert usuario.obtem_atributo(updated_user, "nome") != cpf_invalido, "CPF atualizado, mas não deveria"

# Executa os testes


testa_atualiza_atributo_com_sucesso()
testa_atualiza_atributo_invalido()
