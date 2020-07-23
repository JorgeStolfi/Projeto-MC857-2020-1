import html_botao_simples
import usuario
import compra
import poltrona
import html_botao_simples

def gera(cpr, ver, id_carr):

  cpr_carrinho = ""
  id_cpr = compra.obtem_identificador(cpr)
  usr = compra.obtem_cliente(cpr)
  id_usr = usuario.obtem_identificador(usr)
  atrs_compra = compra.obtem_atributos(cpr)
  preco_tot = compra.calcula_preco(cpr)
  nome_pass = atrs_compra['nome_pass']
  doc_pass = atrs_compra['doc_pass']

  ids_poltronas = poltrona.busca_por_compra(cpr)
  num_poltronas = len(ids_poltronas)

  if(id_cpr == id_carr):
    cpr_carrinho = "&#128722;"

  # !!! Definir um estilo decente para os campos? Ou definir fora do {html_table}? !!!
  ht_carrinho = cpr_carrinho
  ht_cpr = id_cpr
  ht_usr = id_usr
  ht_num_poltronas = str(num_poltronas)
  ht_preco_tot = str(preco_tot)
  ht_nome_pass = nome_pass
  ht_doc_pass = doc_pass
  
  campos = [ht_carrinho, ht_cpr, ht_usr, ht_num_poltronas, ht_nome_pass, ht_doc_pass, ht_preco_tot ]
  
  if ver:
    ht_ver = html_botao_simples.gera("Ver", "ver_compra", {'id_compra': id_cpr}, "#22ff22")
    campos.append(ht_ver)
    
  return campos
