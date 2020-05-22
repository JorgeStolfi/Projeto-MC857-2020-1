import html_resumo_de_trecho_IMP

def gera(trc):
  """Retorna um fragmento HTML que descreve os dados principais de um 
  pedido de compra: identificadores da compra e do cliente, número de
  itens (bilhetes, poltronas), e preço total.  Não mostra a lista de 
  poltronas.
  
  O resultado é uma tupla com fragmentos separados para cada um desses
  campos, que pode ser usada como uma linha do argumento de {html_tabela.gera}."""
  return html_resumo_de_trecho_IMP.gera(trc)
