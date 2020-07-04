#! /usr/bin/python3

import comando_encerrar_trecho
import tabelas
import trecho
import poltrona
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

# Sessao de teste do usuário admin
ses = sessao.busca_por_identificador("S-00000004")

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_encerrar_trecho
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

def testa_encerra_trecho():

    args = {
        'id_trecho': "T-00000001"
    }

    # Executa comando de teste
    testa("Suc", ses, args)

    # Valida se teste funcionou
    updated_trecho = trecho.busca_por_identificador("T-00000001")

    # Pega ids das poltronas de um trecho
    pols_ids = poltrona.busca_por_trecho(updated_trecho)

    # Para cada id de poltrona
    todasAsOfertasApagadas = True
    for pol_id in pols_ids:

        # Pega objeto da poltrona a partir do id
        pol = poltrona.busca_por_identificador(pol_id)

        # confere se a poltrona está com o campo {oferta} == {False}
        pol_oferta = poltrona.obtem_atributo(pol, "oferta")

        if pol_oferta == True:
            todasAsOfertasApagadas = False



    assert todasAsOfertasApagadas, "Nem todas as poltronas tiveram suas ofertas apagadas"

# Executa os testes

testa_encerra_trecho()
