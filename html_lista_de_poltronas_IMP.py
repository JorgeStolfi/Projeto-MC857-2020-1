import poltrona
import html_poltrona
import html_texto
import html_botao_submit
import html_tabela

def gera(ses, cpr, tre, ids):
  linhas = [].copy()
  cmdverProduto = "ver_produto"
  for id_poltrona in ids:
    pol = poltrona.busca_por_identificador(id_poltrona)
    linha = html_poltrona.gera(ses, pol)
    assert type(linha) is list or type(linha) is tuple
    linhas.append(linha)
  ht_itens = html_tabela.gera(linhas)
  return ht_itens
