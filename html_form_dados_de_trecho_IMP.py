import html_label
import html_input
import html_tabela
import html_botao_submit
import html_form_tabela_de_campos
import html_form


def gera(id_trecho, atrs, texto_bt, post_url):
  if id_trecho != None:
    novo = False
    # Inclui campo 'id_trecho' no formulário:
    ht_id_trecho = html_input.gera(None, "hidden", "id_trecho", id_trecho, True, None, None)
  else:
    novo = True
    ht_id_trecho = ""
 

  dados_linhas = (
    ( "Origem",           "text",     "origem",        None,      False, ),
    ( "Destino",          "text",     "destino",       None,      False, ),
  )

  # Monta a tabela com os fragmentos HTML:
  ht_tabela = html_form_tabela_de_campos.gera(dados_linhas, atrs, False)

  ht_bt_buscar = html_botao_submit.gera(texto_bt, post_url, None, '#55ee55')

  ht_campos = \
    ( "    " + ht_id_trecho + "\n" if ht_id_trecho != "" else "") + \
    ht_tabela + \
    ht_bt_buscar

  ht = html_form.gera(ht_campos)
  return ht