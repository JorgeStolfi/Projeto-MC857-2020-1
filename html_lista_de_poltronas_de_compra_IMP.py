import poltrona
import compra
import html_resumo_de_poltrona_de_compra
import html_texto
import html_botao_submit
import html_table

def gera(ids_poltronas, id_compra, excluir, trocar):
  # Validação de argumentos:
  assert id_compra != None
    
  linhas = [].copy()

  # !!! Acrescentar linha de cabeçalho da tabela !!!

  for id_poltrona in ids_poltronas:
    pol = poltrona.busca_por_identificador(id_poltrona)
    
    ver_pol = True
    excluir_pol = excluir
    trocar_pol = trocar
    linha = html_resumo_de_poltrona_de_compra.gera(pol, id_compra, ver_pol, excluir_pol, trocar_pol)
    assert type(linha) is list or type(linha) is tuple

    linhas.append(linha)
    
  ht_res = html_table.gera(linhas)
  return ht_res
