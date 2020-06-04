import poltrona
import html_texto
import html_botao_submit

def gera(pol, ver, excluir):
  atrs_poltrona = poltrona.obtem_atributos(pol)
  id_trecho = atrs_poltrona['id_trecho']
  id_compra = atrs_poltrona['id_compra']
  numero = atrs_poltrona['numero']
  ht_trecho = html_texto.gera(id_trecho, None, None, None, None, None, None, None, None)
  ht_compra = html_texto.gera(id_compra, None, None, None, None, None, None, None, None)
  ht_numero = html_texto.gera(numero, None, None, None, None, None, None, None, None)

  linha = [ ht_trecho, ht_compra, ht_numero ] # Campos da linha, para {html_tabela}
  
  if excluir:
    ht_excluir = html_botao_submit.gera("Excluir", "excluir_poltrona", None, '#bca360')
    linha.append(ht_excluir)

  if ver:
    ht_ver = html_botao_submit.gera("Ver", 'ver_poltrona', None, '#60a3bc')
    linha.append(ht_ver)
    
  return linha
