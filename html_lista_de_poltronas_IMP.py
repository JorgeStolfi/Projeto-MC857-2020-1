import poltrona
import compra
import html_poltrona
import html_texto
import html_botao_submit
import html_tabela

def gera(ses, cpr, trc, ids, excluir):
  # Validação de argumentos
  assert cpr == None or compra.obtem_atributo(cpr, 'status') == 'aberto' or not excluir
    
  linhas = [].copy()
  for id_poltrona in ids:
    pol = poltrona.busca_por_identificador(id_poltrona)
    ver_pol = True # Haverá botão "Ver".
    excluir_pol = excluir
    linha = html_poltrona.gera(ses, pol, ver_pol, excluir_pol)
    assert type(linha) is list or type(linha) is tuple
    linhas.append(linha)
  ht_itens = html_tabela.gera(linhas)
  return ht_itens
