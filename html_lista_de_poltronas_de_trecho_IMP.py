import poltrona
import compra
import usuario
import trecho
import html_resumo_de_poltrona_de_trecho
import html_botao_submit
import html_table

def gera(ids_poltronas, usr, carr):

  id_trc = None # Identificador do trecho comum, ou None.
  
  admin = False if usr == None else usuario.obtem_atributo(usr, 'administrador')
  fazer_checkin = admin # Por enquanto.
  
  if admin or usr == None: assert carr == None # Administrador e não-logado não tem carrinho.
  id_carr = None if carr == None else compra.obtem_identificador(carr)
  
  # Gera a linha de os cabeçalhos das colunas
  linha_cab = html_resumo_de_poltrona_de_trecho.gera_cabecalho(fazer_checkin);
  assert type(linha_cab) is list or type(linha_cab) is tuple # Paranóia.
  
  # Gera as linhas da tabela.
  linhas = [].copy()
  for id_poltrona in ids_poltronas:
    pol = poltrona.busca_por_identificador(id_poltrona)
    
    # Obtem dados da poltrona:
    assert pol != None
    id_trc_pol = poltrona.obtem_atributo(pol, 'id_trecho')
    id_cpr_pol = poltrona.obtem_atributo(pol, 'id_compra')
    cpr_pol = None if id_cpr_pol == None else compra.busca_por_identificador(id_cpr_pol)
    usr_pol = None if cpr_pol == None else compra.obtem_cliente(cpr_pol)
    
    # Verifica se o trecho é o mesmo para todas as poltronas:
    if id_trc != None: assert id_trc_pol == id_trc
    id_trc = id_trc_pol
    
    # Decide que botões vai ter:
    alterar = admin
    comprar = (carr != None) and poltrona.pode_comprar(usr, pol, carr)
    excluir = (cpr_pol != None) and (usr_pol == usr) and poltrona.pode_excluir(usr, pol)
    
    # Gera os campos da linha:
    linha = html_resumo_de_poltrona_de_trecho.gera(pol, alterar, comprar, excluir, fazer_checkin)
    assert type(linha) is list or type(linha) is tuple # Paranóia.
    linhas.append(linha)

  ht_tabela = html_table.gera(linhas, linha_cab)
  ht_legenda = html_resumo_de_poltrona_de_trecho.gera_legenda(fazer_checkin)
  ht_res = ht_tabela + ht_legenda
  return ht_res
