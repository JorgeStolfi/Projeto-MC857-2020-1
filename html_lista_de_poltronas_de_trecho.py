
import html_lista_de_poltronas_de_trecho_IMP

def gera(ids_poltronas, id_trecho, alterar, comprar, id_compra):
  """Retorna um trecho de HTML que descreve as poltronas cujos identificadores
  estão na lista {ids_poltronas}.  Todas as poltronas devem pertencer ao 
  trecho cujo identficador é {id_trecho}, que supõe-se ter sido
  identificado separadamente.
  
  O resultado é um elemento "<table>...</table>". Cada
  linha é gerada por {html_resumo_de_poltrona_de_trecho.gera}
  com argumentos {(pol, id_trecho, alterar, comprar, id_compra)}, e 
  tem os número da poltrona, o preço, o pedido de compra
  que atualmente inclui a poltrona, indicação de oferta, 
  além dos botões solicitados por {alterar} e {comprar}."""
  return html_lista_de_poltronas_de_trecho_IMP.gera(ids_poltronas, id_trecho, alterar, comprar, id_compra)
