import html_pag_generica
import html_div
import html_estilo_cabecalho_de_tabela
import sys
import utils_testes
from utils_testes import mostra


def processa(ses, msg):
    # cria mensagem de resposta
    html_msg = html_div.gera(html_estilo_cabecalho_de_tabela.gera(), "Obrigado pela mensagem")
    pag = html_pag_generica.gera(ses, html_msg, None)

    #escreve a mensagem em {stderr}
    mostra(0, "msg de contato = " + str(msg) + "")
    return pag
