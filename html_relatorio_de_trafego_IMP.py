
import html_table

def gera(dados):

    # Converte dados no formato gerado por {trecho.resumo_de_trafego} para
    # formato aceito por {html_table}
    ht_linhas = [].copy()
    for dado in dados:
        linha = [].copy()

        # Codigo do aeroporto
        linha.append(dado[0])

        # Infos de chegada
        for rel_chegada_item in dado[1]:
            linha.append(rel_chegada_item)

        # Infos de saida
        for rel_saida_item in dado[2]:
            linha.append(rel_saida_item)

        ht_linhas.append(linha)

    ht_table = html_table.gera(ht_linhas, ["Aeroporto", "# de trechos (chegada)", "# total de poltronas (chegada)", "# de poltronas reservadas (chegada)", "Total dos preços das poltronas reservadas (chegada)", "# de passageiros que fizeram checkin (chegada)", "# de trechos (saida)", "# total de poltronas (saida)", "# de poltronas reservadas (saida)", "Total dos preços das poltronas reservadas (saida)" , "# de passageiros que fizeram checkin (saida)"])
    return ht_table
