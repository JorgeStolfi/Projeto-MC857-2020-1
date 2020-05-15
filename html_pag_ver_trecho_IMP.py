import html_pag_generica
import html_bloco_texto
import html_paragrafo
import html_tabela
# import html_bloco_lista_de_assentos

from trecho import obtem_atributos, obtem_assentos

def gera(sessao, obj_trecho):

    # estilos
    estilo_parag = "\n display:block; word-wrap:break-word;  width: 100%;\n  margin-top: 10px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  line-height: 75%;"

    # gerando tabela
    titulos = ("Código", "Origem", "Destino", "Data de Partida", "Data de Chegada")
    atributos = obtem_atributos(obj_trecho)
    linhas = []
    for titulo, valor in zip(titulos, atributos.values()):
        ht_titulo = html_paragrafo.gera(estilo_parag, html_bloco_texto.gera(titulo, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))
        ht_valor = html_paragrafo.gera(estilo_parag, html_bloco_texto.gera(valor, None, "Courier", "20px", None, "2px", "left", "#263238", None))
        linhas.append([ht_titulo, ht_valor])

    tabela = html_tabela.gera(linhas)

    # ids = obtem_assentos(obj_trecho)
    ids = []
    assentos = ""
    # assentos = html_bloco_lista_de_assentos.gera(sessao, None, obj_trecho, ids, False)

    conteudo = tabela + "<br/>" + assentos

    return html_pag_generica.gera(sessao, tabela, None)
