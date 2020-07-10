import poltrona
import html_resumo_de_poltrona_de_usuario
import html_table
import html_div

def gera(ids_poltronas):

  linhas = [].copy()

  # Cabeçalho:
  estilo_cab = "font-size:20px;font-weight:bold; padding:0px 10px 0px 0px"
  cabs_raw = [ 'Trecho', 'Origem', 'Partida', 'Destino', 'Chegada', 'Poltrona', 'Preço', 'Ver Poltrona']
  cabs_div = [].copy()
  for cb in cabs_raw:
    cabs_div.append(html_div.gera(estilo_cab, cb))

  for id_poltrona in ids_poltronas:
    pol = poltrona.busca_por_identificador(id_poltrona)

    linha = html_resumo_de_poltrona_de_usuario.gera(pol)
    assert type(linha) is list or type(linha) is tuple

    linhas.append(linha)

  ht_res = html_table.gera(linhas, cabs_div)
  return ht_res
