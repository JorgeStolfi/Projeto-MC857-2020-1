
import html_input
import html_botao_submit
import html_form_tabela_de_campos
import html_form

def gera(atrs, admin):

    dados_linhas = (
        ( "Origem",           "text",        "origem",          "Cidade, aeroporto",    False, ),
        ( "Detino",           "text",        "destino",         "Cidade, aeroporto",    False, ),
        ( "Data",             "data",        "data",            "xx/xx/xxxx",           False, ),
        ( "Horario",          "horario",     "horario",         "xx:xx",                False, ),
        )

      ht_tabela = html_form_tabela_de_campos.gera(dados_linhas, atrs, admin)
      ht_submit = html_botao_submit.gera("Buscar", atrs, None, '#55ee55')

      ht_campos = \
            ht_tabela + \
            ht_submit

      return html_form.gera(ht_campos)
