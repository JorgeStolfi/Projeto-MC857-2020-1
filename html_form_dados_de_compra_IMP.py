import compra
import usuario
import poltrona
import html_input
import html_form_table
import html_botao_submit
import html_botao_simples
import html_form

def gera(cpr, admin, texto_bt, comando_bt):

  id_cpr = compra.obtem_identificador(cpr)
  atrs_cpr = compra.obtem_atributos(cpr)
  ids_poltronas = compra.obtem_poltronas(cpr)

  # Parâmetros gerais da compra:
  status_cpr = atrs_cpr['status']
  # !!! Deveria obter origem e partida do primeiro trecho, destino e chegada do último trecho. !!!
  preco_tot_cpr = compra.calcula_preco(cpr)
  
  usr = compra.obtem_cliente(cpr)
  id_usr = usuario.obtem_identificador(usr)
  num_trechos = len(ids_poltronas)

  ht_id_cpr = html_input.gera(None, "readonly", "id_compra",  id_cpr, True, None, None)
  ht_id_usr = html_input.gera(None, "readonly", "id_usuario", id_usr, True, None, None)
  
  ht_status = "Status: " + str(status_cpr)
  ht_num_trechos = "Trechos: " + str(num_trechos)
  ht_preco = "Preco total: " + str(preco_tot_cpr)
  dados_linhas = \
    (
      ( "Passageiro", "text", "nome_pass",     "Nome e sobrenome",  False),
    )
  ht_table = html_form_table.gera(dados_linhas, atrs_cpr, admin)

  ht_submit = html_botao_submit.gera(texto_bt, comando_bt, None, '#55ee55')

  ht_cancel = html_botao_simples.gera("Cancelar", 'principal', None, '#ee5555')

  ht_campos = \
    ( "    <p>" + ht_status + "\n</p>" ) + \
    ( "    " + ht_id_usr + "\n" if ht_id_usr != "" else "") + \
    ( "    " + ht_id_cpr + "\n" if ht_id_cpr != "" else "") + \
    ( ht_table + "\n" ) + \
    ( "    " + ht_num_trechos + "\n" ) + \
    ( "    " + ht_preco + "\n" ) + \
    ( "    " + ht_submit + "\n" ) + \
    ( "    " + ht_cancel + "\n" )
  
  return html_form.gera(ht_campos)
