import poltrona
import compra
import html_resumo_de_poltrona_de_compra
import html_texto
import html_botao_submit
import html_table
import html_div

def gera(ids_poltronas, id_compra, excluir, trocar):
  # Validação de argumentos:
  assert id_compra != None

  linhas = [].copy()

  # Cabeçalho:
  estilo_cab = "font-size:20px;font-weight:bold; padding:0px 10px 0px 0px"
  cabs_raw = [ 'Poltrona', 'ID da Compra', 'Ver Poltrona', 'Excluir Poltrona', 'Trocar Poltrona']
  cabs_div = [].copy()
  for cb in cabs_raw:
    cabs_div.append(html_div.gera(estilo_cab, cb))

  linhas.append(cabs_div)

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
