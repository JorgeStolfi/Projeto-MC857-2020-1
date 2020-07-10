import poltrona
import compra
import html_resumo_de_poltrona_de_trecho
import html_texto
import html_botao_submit
import html_table
import html_div

def gera(ids_poltronas, id_trecho, alterar_pols, comprar_pols, id_compra):
  # Validação de argumentos:
  assert id_trecho != None
  assert (not comprar_pols) or (id_compra != None)

  linhas = [].copy()

  #estilo do cabeçalho e aplicação do estilo
  # !!! Definir função  {hrml_estilo_cabecalho_de_tabela.gera} !!!
  estilo_cab = "font-size:20px;font-weight:bold; background-color: #60a3bc; color: white; padding:0px 10px 0px 0px"
  cabs_raw = [ 'Poltrona', 'Preço', '', 'Compra']
  cabs_div = [].copy()

  #aplicar estilos nas colunas
  for cb in cabs_raw:
    cabs_div.append(html_div.gera(estilo_cab, cb))

  # Determina se alguma poltrona neste trecho já está reservada para esta compra:
  ja_comprou_trc = False # !!! Consertar !!!
  
  # Gera as linhas da tabela.
  for id_poltrona in ids_poltronas:
    pol = poltrona.busca_por_identificador(id_poltrona)
    alterar_pol = alterar_pols
    comprar_pol = comprar_pols and (not ja_comprou_trc)
    trocar_pol = comprar_pols and ja_comprou_trc
    linha = html_resumo_de_poltrona_de_trecho.gera \
      (pol, id_trecho, alterar_pol, comprar_pol, trocar_pol, id_compra)
    assert type(linha) is list or type(linha) is tuple

    linhas.append(linha)

  ht_res = html_table.gera(linhas, cabs_div)
  return ht_res
