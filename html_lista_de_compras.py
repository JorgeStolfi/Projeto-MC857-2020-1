
import html_lista_de_compras_IMP

def gera(ids_compras, ver):
  """Retorna um trecho de HTML que descreve as compras cujos
  identificadores são os elementos da lista {ids}.

  O resultado é uma tabela HTML ("<table>...</table>") em que cada 
  linha é o resumo de uma compra {cpr}, montado pela
  funcao {html_resumo_de_compra.gera}.  
  
  Se {ver} for {True}, cada linha terá um botão "Ver" que, quando
  clicado, emitrá o comando "ver_compra" com o identificador de 
  compra como argumento."""
  return html_lista_de_compras_IMP.gera(ids_compras, ver)
