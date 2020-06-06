import poltrona
import compra
import html_resumo_de_poltrona
import html_texto
import html_botao_submit
import html_table

def gera(ids, cpr, trc, excluir, trocar):
  # Validação de argumentos
  assert cpr == None or compra.obtem_atributo(cpr, 'status') == 'aberto' or not excluir
    
  linhas = [].copy()
  for id_poltrona in ids:
    pol = poltrona.busca_por_identificador(id_poltrona)
    ver_pol = True # Haverá botão "Ver".
    excluir_pol = excluir
    trocar_pol = trocar
    linha = html_resumo_de_poltrona.gera(pol, ver_pol, excluir_pol, trocar_pol)
    assert type(linha) is list or type(linha) is tuple
    linhas.append(linha)
  ht_itens = html_table.gera(linhas)
  return ht_itens
