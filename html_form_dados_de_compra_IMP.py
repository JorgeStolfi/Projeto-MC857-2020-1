import compra
import usuario
import poltrona
import trecho
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
  
  # pega ids dos trechos das poltronas
  ids_trechos = []
  for id in ids_poltronas:
    p_aux = poltrona.busca_por_identificador(id)
    ids_trechos.append(poltrona.obtem_atributo(p_aux, 'id_trecho'))

  # obtem trechos
  trechos = []
  for id in ids_trechos:
    trechos.append(trecho.busca_por_identificador(id))

  # obtem atributos do primeiro e ultimo trechos
  first_trecho_attrs = trecho.obtem_atributos(trechos[0])
  last_trecho_attrs = trecho.obtem_atributos(trechos[len(trechos) - 1])

  preco_tot_cpr = compra.calcula_preco(cpr)
  
  usr = compra.obtem_cliente(cpr)
  id_usr = usuario.obtem_identificador(usr)
  num_trechos = len(ids_poltronas)

  ht_id_cpr = html_input.gera(None, "readonly", "id_compra",  id_cpr, True, None, None)
  ht_id_usr = html_input.gera(None, "readonly", "id_usuario", id_usr, True, None, None)
  
  ht_num_trechos = "Trechos: " + str(num_trechos)
  ht_firts_trecho = "Origem: " + str(first_trecho_attrs['origem']) + " Partida: " + str(first_trecho_attrs['dia_partida']) + " " + str(first_trecho_attrs['hora_partida'])
  ht_last_trecho = "Destino: " + str(last_trecho_attrs['destino']) + " Chegada: " + str(last_trecho_attrs['dia_chegada']) + " " + str(last_trecho_attrs['hora_chegada'])
  ht_preco = "Preco total: " + str(preco_tot_cpr)
  dados_linhas = \
    (
      ( "Passageiro", "text", "nome_pass",     "Nome e sobrenome",  False),
    )
  ht_table = html_form_table.gera(dados_linhas, atrs_cpr, admin)

  ht_submit = html_botao_submit.gera(texto_bt, comando_bt, None, '#55ee55')

  ht_cancel = html_botao_simples.gera("Cancelar", 'principal', None, '#ee5555')

  ht_campos = \
    ( "    " + "ID Usuario: " + ht_id_usr + "</br>" if ht_id_usr != "" else "") + \
    ( "    " + "ID Compra: " + ht_id_cpr + "</br>" if ht_id_cpr != "" else "") + \
    ( ht_table + "</br>" ) + \
    ( "    " + ht_num_trechos + "</br>" ) + \
    ( "    " + ht_firts_trecho + "</br>" ) + \
    ( "    " + ht_last_trecho + "</br>" ) + \
    ( "    " + ht_preco + "</br>" ) + \
    ( "    " + ht_submit + "</br>" ) + \
    ( "    " + ht_cancel + "</br>" )
  
  return html_form.gera(ht_campos)
