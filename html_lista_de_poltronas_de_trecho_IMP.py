import poltrona
import compra
import html_resumo_de_poltrona_de_trecho
import html_texto
import html_botao_submit
import html_table

def gera(ids_poltronas, id_trecho, alterar, comprar, id_compra):
  # Validação de argumentos:
  assert id_trecho != None
  assert (not comprar) or (id_compra != None)

  linhas = [].copy()

  # !!! Acrescentar uma linha de cabeçalho !!!

  for id_poltrona in ids_poltronas:
    pol = poltrona.busca_por_identificador(id_poltrona)
    
    comprar_pol = comprar
    alterar_pol = alterar
    linha = html_resumo_de_poltrona_de_trecho.gera(pol, id_trecho, alterar_pol, comprar_pol, id_compra)
    assert type(linha) is list or type(linha) is tuple

    linhas.append(linha)
    
  ht_res = html_table.gera(linhas)
  return ht_res
