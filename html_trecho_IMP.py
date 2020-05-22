import trecho
import html_texto
import poltrona
import html_lista_de_poltronas
import html_resumo_de_trecho
import html_tabela

def gera(ses, trc, detalhe):
  linha_resumo = html_resumo_de_trecho.gera(trc)

  if detalhe:
    # Cabeçalho como bloco texto + lista de poltronas:
    ht_resumo = " ".join(linha_resumo) 
    pols = poltrona.busca_por_trecho(trc)
    ht_pols = html_lista_de_poltronas.gera(ses, None, trc, pols)
    return ht_resumo + "<br/>" + ht_pols
  else:
    # Só cabeçalho, como lista de campos para {html_table.gera}
    return linha_resumo
