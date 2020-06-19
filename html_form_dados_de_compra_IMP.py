import compra
import usuario
import poltrona
import html_input
import html_form_table
import html_botao_submit
import html_botao_simples
import html_form
import html_texto

def gera(cpr, admin, texto_bt, comando_bt):

  id_cpr = compra.obtem_identificador(cpr)
  atrs_cpr = compra.obtem_atributos(cpr)
  ids_poltronas = compra.obtem_poltronas(cpr)
  num_trechos = len(ids_poltronas)

  # Parâmetros gerais da compra:
  status_cpr = atrs_cpr['status']
  # !!! Deveria obter origem e partida do primeiro trecho, destino e chegada do último trecho. !!!
  preco_tot_cpr = compra.calcula_preco(cpr)

  usr = compra.obtem_cliente(cpr)
  id_usr = usuario.obtem_identificador(usr)
  atrs_usr = usuario.obtem_atributos(usr)

  # Montando o formulário
  ht_id_cpr = html_input.gera("Id da Compra", "readonly", "id_compra",  id_cpr, True, None, None)
  ht_id_usr = html_input.gera("Id do Usuário", "readonly", "id_usuario", id_usr, True, None, None)
  ht_nome_usr = html_input.gera("Usuário", "readonly", "nome_usuario", atrs_usr['nome'], True, None, None)
  ht_num_trechos = html_input.gera("Número de Trechos", "readonly", "num_trechos", num_trechos, True, None, None)
  ht_preco = html_input.gera("Total da Compra", "readonly", "preco_total", preco_tot_cpr, True, None, None)

  ht_submit = html_botao_submit.gera(texto_bt, comando_bt, None, '#55ee55')
  ht_cancel = html_botao_simples.gera("Cancelar", 'principal', None, '#ee5555')

  # Formatando HTML
  ht_campos = ''
  ht_campos += ht_id_cpr + '<br>'
  ht_campos += ht_id_usr + '<br>'
  ht_campos += ht_nome_usr + '<br>'
  ht_campos += ht_num_trechos + '<br>'
  ht_campos += ht_preco + '<br>'

  # Não deve aparecer na página do carrinho
  # ht_campos += ht_submit + '<br>'
  # ht_campos += ht_cancel + '<br>'

  return html_form.gera(ht_campos)
