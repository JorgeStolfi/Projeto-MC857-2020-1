import html_resumo_de_sessao_IMP

def gera(ses, bt_ver, bt_fechar):
  """Retorna HTML que descreve dados principais de uma
  sessão: identificador da sessão, usuário dono da sessão, um booleano
  indicando se a sessão está aberta ou não, o cookie da sessão, o identificador
  do carrinho associado à sessão e a data de criação da sessão. Além disso,
  botões para ver detalhes da sessão e para fechá-la (caso esteja aberta)
  também são retornados, de acordo com os valores dos parâmetros {bt_ver} e
  {bt_fechar}

  O resultado é uma tupla com fragmentos separados para cada um desses
  campos, que pode ser usada como uma linha do argumento de {html_table.gera}.

  Se {bt_ver} é {True}, um dos elementos da tupla será um fragmento HTML
  que descreve um botão "Ver". Quando clicado, esse botão emitirá o comando
  HTTP "ver_detalhes_sessao" com o identificador da sessão como argumento.

  Se {bt_fechar} é {True}, um dos elementos da tupla será um fragmento HTML
  que descreve um botão "Fechar". Quando clicado, esse botão emitirá o comando
  HTTP "fechar_sessao" com o identificador da sessão como argumento.

  (Os parãmetros {bt_ver,bt_fechar} só deveriam ser
  {True} se o usuário da sessão corrente for um administrador.)"""
  return html_resumo_de_sessao_IMP.gera(ses, bt_ver, bt_fechar)
