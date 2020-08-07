
import html_estilo_cabecalho_de_tabela
import html_pag_generica
import html_span
import html_table

def gera(ses, dados):

  # Converte dados no formato gerado por {trecho.resumo_de_trafego} para
  # formato aceito por {html_table}
  estilo_item = "font-family:Courier;font-size:20;"
  ht_linhas_dados = [].copy()
  for dado in dados:
    linha_porto = [].copy()
    # Codigo do aeroporto
    linha_porto.append(html_span.gera(estilo_item, str(dado[0])))

    # Infos de chegada
    for ch_item in dado[1]:
      linha_porto.append(html_span.gera(estilo_item, str(ch_item)))

    # Infos de saida
    for sa_item in dado[2]:
      linha_porto.append(
        html_span.gera(estilo_item, str(sa_item)))

    ht_linha_porto = [html_span.gera(estilo_item, x) for x in linha_porto]

    ht_linhas_dados.append(ht_linha_porto)
    
  linha_cab = [].copy();
  linha_cab.append("Aeroporto")
  for lado in ("chegada", "saida"):
    for tt in ( \
        "# de trechos",  \
        "# total de poltronas", \
        "# de poltronas reservadas",  \
        "Total dos preços das poltronas reservadas",  \
        "# de passageiros que fizeram checkin" \
      ):
      linha_cab.append(tt + " (" + lado + ")")
   
  estilo_cab = html_estilo_cabecalho_de_tabela.gera()
  ht_linha_cab = map(lambda x : html_span.gera(estilo_cab, x), linha_cab)

  ht_table = html_table.gera(ht_linhas_dados, ht_linha_cab)
  return html_pag_generica.gera(ses, ht_table, None)
