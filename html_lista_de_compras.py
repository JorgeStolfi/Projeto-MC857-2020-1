
import html_lista_de_compras_IMP

def gera(ids_compras, ver, trocar):
  """Retorna um trecho de HTML que descreve as compras cujos
  identificadores são os elementos da lista {ids}.

  O resultado é uma tabela HTML ("<table>...</table>") em que cada 
  linha é o resumo de uma compra {cpr}, montado pela
  funcao {html_resumo_de_compra.gera}.  
  
  Se {ver} e {trocar} for {True}, cada linha terá um botão "Ver" e "Trocar".
  Botao "Ver" quando clicado, emitrá o comando "ver_compra" com o identificador de 
  compra como argumento.
  Botao "Trocar" quando clicado, emitrá o comando "trocar_poltrona" com o identificador de 
  compra como argumento."""
  return html_lista_de_compras_IMP.gera(ids_compras, ver, trocar)
