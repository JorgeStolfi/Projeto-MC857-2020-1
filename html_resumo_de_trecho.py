import html_resumo_de_trecho_IMP

def gera(trc, ver, alterar, clonar):
  """Retorna HTML que descreve dados principais de um 
  trecho: identificadores do trecho, da compra e do cliente, número de
  total de poltronas, número de poltronas livres, e intervalo
  de preços destas últimas.  Não mostra a lista de poltronas.
  
  Se {ver} é {True}, um dos elementos da tupla será um fragmento HTML
  que descreve um botão "Ver". Quando clicado, esse botão emitirá o comando
  HTTP "ver_trecho" com o identificador do trecho como argumento.
  
  Se {alterar} é {True}, um dos elementos da tupla será um fragmento HTML
  que descreve um botão "Alterar ". Quando clicado, esse botão emitirá o comando
  HTTP "alterar_trecho" com o identificador do trecho como argumento.

  Se {clonar} é {True}, um dos elementos da tupla será um fragmento HTML
  que descreve um botão "Clonar ". Quando clicado, esse botão emitirá o comando
  HTTP "clonar_trecho" com o identificador do trecho como argumento.
  
  O resultado é uma tupla com fragmentos separados para cada um desses
  campos, que pode ser usada como uma linha do argumento de {html_table.gera}."""
  return html_resumo_de_trecho_IMP.gera(trc, ver, alterar, clonar)
