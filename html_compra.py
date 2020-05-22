import html_compra_IMP

def gera(cpr, detalhe):
  """Retorna um fragmento HTML que descreve um pedido de compra.

  Se {detalhe} for {False}, devolve apenas o resumo da compra.
  
  Se{detalhe} for {True}, mostra também a lista de 
  poltronas."""
  return html_compra_IMP.gera(cpr, detalhe)
