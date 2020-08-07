
import html_botao_submit
import html_botao_simples
import html_form_table
import html_form

def gera(atrs, admin):

  # Dados para {html_form_table.gera}
  # {(rotulo,tipo,chave,dica,visivel,editavel,obrigatorio)}
  dados_linhas = (
    ( "Usuário",  "text",   "id_usuario",  "U-xxxxxxxx",  True, True, True, ),
 )

  ht_table = html_form_table.gera(dados_linhas, atrs)
  ht_submit = html_botao_submit.gera("Buscar", "buscar_compras", None, '#55ee55')
  ht_cancel = html_botao_simples.gera("Cancelar", "principal", None, '#ff2200')

  ht_conteudo = \
        ht_table + \
        ht_submit + \
        ht_cancel

  return html_form.gera(ht_conteudo)
