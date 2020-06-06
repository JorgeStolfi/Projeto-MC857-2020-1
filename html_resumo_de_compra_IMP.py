import html_botao_simples
import usuario
import compra
import poltrona
import html_botao_simples

def gera(cpr, ver):
  id_cpr = compra.obtem_identificador(cpr)
  usr = compra.obtem_cliente(cpr)
  id_usr = usuario.obtem_identificador(usr)
  atrs_compra = compra.obtem_atributos(cpr)
  valor = compra.calcula_preco(cpr)

  ids_poltronas = poltrona.busca_por_compra(cpr)
  num_poltronas = len(ids_poltronas)

  ht_cpr = id_cpr
  ht_usr = id_usr
  ht_num_poltronas = str(num_poltronas)
  ht_preco = str(valor)
  ht_nome_pass = atrs_compra['nome_pass']
  campos = [ ht_cpr, ht_usr, ht_num_poltronas, ht_nome_pass, preco ]
  
  if ver:
    ht_ver = html_botao_simples.gera("Ver", "ver_compra", {'id_compra': id_cpr}, "#22ff22")
    campos.append(ht_ver)
    
  return campos
