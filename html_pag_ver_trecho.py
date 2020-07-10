import html_pag_ver_trecho_IMP

def gera(ses, trc, comprar, alterar, erros):
  """Retorna uma página HTML que mostra os dados do trecho {trc}
  (que deve ser um objeto de tipo {Objeto_Trecho}).

  A página terá um cabeçalho com resumo das informações do trecho
  (vide {html_resumo_de_trecho.gera}), em seguida uma lista das poltronas
  do trecho.

  O parâmetro {comprar} só deveria ser {True} se a sessão {ses} estiver
  aberta e o dono NÃO for administrador. Se for {True}, cada poltrona
  livre terá um botão "Comprar" que, quando clicado, emitirá o comando
  "solicitar_pag_comprar_bilhete" com o identificador da potrona como
  argumento 'id_poltrona' e o identificador do carrinho da sessão
  como argumento 'id_compra'.

  O parâmetro {alterar} só deveria ser {True} se o dono da sessão {ses} for
  um administrador. Se for {True}, cada poltrona terá um boão "Alterar" que,
  quando clicado, emitirá o comando "solicitar_pag_alterar_potrona".
  Haverá também na página um botão "Alterar", que emitirá o comando 
  "solicitar_pag_alterar_trecho"; um botão "Clonar" que emite o comando 
  "solicitar_pag_clonar_trecho"; e um botão "Encerrar" que emite o comando
  "encerrar_trecho".   Estes comandos vão receber o identificador {id_trecho}
  do trecho {trc}."""
  return html_pag_ver_trecho_IMP.gera(ses, trc, comprar, alterar, erros)
