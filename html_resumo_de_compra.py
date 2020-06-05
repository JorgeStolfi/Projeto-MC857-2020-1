import html_resumo_de_compra_IMP

def gera(cpr, ver, trocar):
  """Retorna um fragmento HTML que descreve os dados principais de um 
  pedido de compra {cpr}: identificadores da compra e do cliente, número de
  itens (bilhetes, poltronas), e preço total.  Não mostra a lista de 
  poltronas.
  
  O resultado é uma lista de strings, uma para cada atributo, que pode
  ser incluída como uma linha para {html_table.gera}."""
  return html_resumo_de_compra_IMP.gera(cpr, ver, trocar)
