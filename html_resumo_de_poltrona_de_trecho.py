import html_resumo_de_poltrona_de_trecho_IMP

def gera(pol, id_trecho, alterar, comprar, id_compra):
  """Devolve um fragmento HTML que decreve a poltrona {pol},
  um objeto da classe {Objeto_Poltrona}.  A poltrona deve pertencer ao
  trecho {id_trecho}.

  O fragmento mostra o número da poltrona, o identificador do pedido de
  compra para o qual foi reservado (p. ex. "C-00002322" ou "LIVRE"),
  e o preço.

  Se a poltrona for uma oferta, mostra também uma indicação desse fato.

  Se {alterar} for {True}, a linha terá um botão "Alterar"
  que, quando clicado, emitirá o comando HTTP "solicitar_pag_alterar_poltrona", com
  argumento {'id_poltrona': id_poltrona}.  (Normalmente, este botão
  só deveria ser solicitado se o dono da sessão corrente for um administrador.)

  Se {comprar} for {True} e a poltrona estiver livre,
  a linha terá um botão "Comprar" que, quando clicado, emitirá o comando HTTP
  "comprar_poltrona", com argumentos {'id_poltrona': id_poltrona,
  'id_compra': id_compra}.  (Normalmente, este botão só deveria ser
  solicitado se o dono da sessão corrente for um cliente comum,
  e ele for o dono do pedido de compra {id_compra}, e este
  estiver em aberto.)

  Em qualquer caso, será monstrado um botão "Ver", que, quando clicado,
  emite of comando HTTP "ver_poltrona", com
  argumento {'id_poltrona': id_poltrona}.

  O resultado não é um string, mas uma tupla com um string separado
  para cada campo ou botão.  Esta tupla deve ser usada como uma linha do
  argumento de {html_table}."""
  return html_resumo_de_poltrona_de_trecho_IMP.gera(pol, id_trecho, alterar, comprar, id_compra)
