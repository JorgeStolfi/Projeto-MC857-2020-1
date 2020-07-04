import html_pag_ver_trecho_IMP

def gera(ses, trc, comprar, alterar, erros):
  """Retorna uma página HTML que mostra os dados do trecho {trc}
  (que deve ser um objeto de tipo {Objeto_Trecho}).

  A página terá um cabeçalho com resumo das informações do trecho
  (vide {html_resumo_de_trecho.gera}), em seguida uma lista das poltronas
  do trecho e por fim um botão "Encerrar" que ao ser clicado emite o comando {encerrar_trecho} passando como o argumento de URL {id_trecho} o id do trecho que originou a ação.

  Se {comprar} for {True}, cada poltrona terá um botão "Comprar" que,
  quando clicado, emitirá o comando "solicitar_pag_comprar_bilhete" com o identificador
  da potrona como argumento.

  Se {alterar} for {True}, cada poltrona terá um boão "Alterar" que,
  quando clicado, emitirá o comando "solicitar_pag_alterar_potrona". 
  Haverá também um botão "Alterar" no cabeçalho, que emitirá o comando 
  "solicitar_pag_alterar_trecho".
  
  Se o usuário for administrador, mostrar um botão 'Clonar' para clonar o trecho."""
  return html_pag_ver_trecho_IMP.gera(ses, trc, comprar, alterar, erros)
