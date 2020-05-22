import poltrona
import html_texto
import html_botao_submit

def gera(pol):
  atrs_poltrona = poltrona.obtem_atributos(pol)
  id_trecho = atrs_poltrona['id_trecho']
  id_compra = atrs_poltrona['id_compra']
  numero = atrs_poltrona['numero']
  ht_trecho = html_texto.gera(id_trecho, None, None, None, None, None, None, None, None)
  ht_compra = html_texto.gera(id_compra, None, None, None, None, None, None, None, None)
  ht_numero = html_texto.gera(numero, None, None, None, None, None, None, None, None)
  ht_exlcuir = html_botao_submit.gera("Excluir", "excluir_poltrona", None, '#bca360')
  ht_comprar = html_botao_submit.gera("Comprar", 'comprar_poltrona', None, '#60a3bc')
  linha = ( ht_trecho, ht_compra, ht_numero, ht_exlcuir, ht_comprar ) 
  return linha
