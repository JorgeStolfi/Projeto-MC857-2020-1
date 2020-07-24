
import html_lista_de_compras_IMP

def gera(ids_compras, ver, id_carrinho):
  """Retorna um trecho de HTML que descreve os pedidos de compras cujos
  identificadores são os elementos da lista {ids_compras}.

  O resultado é uma tabela HTML ("<table>...</table>") em que cada 
  linha é o resumo de um pedido de compra {cpr}, montado pela
  funcao {html_resumo_de_compra.gera}.  
  
  Se {ver} for {True}, cada linha terá um botão "Ver" que,
  quando clicado, emitrá o comando "ver_compra" com o identificador de 
  compra como argumento.

  {id_carrinho} é o identificador da compra que deve ser identificada
  como o carrinho atual.  Pode ser {None}."""
  return html_lista_de_compras_IMP.gera(ids_compras, ver, id_carrinho)
