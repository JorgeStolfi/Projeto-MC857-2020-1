import html_resumo_de_trecho_IMP

def gera(trc, bt_ver, bt_alterar, bt_clonar, bt_fechar):
  """Retorna HTML que descreve dados principais de um 
  trecho: identificadores do trecho, da compra e do cliente, número de
  total de poltronas, número de poltronas livres, e intervalo
  de preços destas últimas.  Não mostra a lista de poltronas.
  
  O resultado é uma tupla com fragmentos separados para cada um desses
  campos, que pode ser usada como uma linha do argumento de {html_table.gera}.
  
  Se {bt_ver} é {True}, um dos elementos da tupla será um fragmento HTML
  que descreve um botão "Ver". Quando clicado, esse botão emitirá o comando
  HTTP "ver_trecho" com o identificador do trecho como argumento.
  
  Se {bt_alterar} é {True}, um dos elementos da tupla será um fragmento HTML
  que descreve um botão "Alterar ". Quando clicado, esse botão emitirá o comando
  HTTP "solicitar_pag_alterar_trecho" com o identificador do trecho como argumento.

  Se {bt_clonar} é {True}, um dos elementos da tupla será um fragmento HTML
  que descreve um botão "Clonar ". Quando clicado, esse botão emitirá o comando
  HTTP "solicitar_pag_clonar_trecho" com o identificador do trecho como argumento.
  
  Se {bt_fechar} é {True}, um dos elementos da tupla será um fragmento HTML
  que descreve um botão "Encerrar". Quando clicado, esse botão emitirá o comando
  HTTP "fechar_trecho" com o identificador do trecho como argumento.
  
  (Os parãmetros {bt_alterar,bt_clonar,bt_fechar} só deveriam ser
  {True} se o usuário da sessão corrente for um administrador.)"""
  return html_resumo_de_trecho_IMP.gera(trc, bt_ver, bt_alterar, bt_clonar, bt_fechar)
