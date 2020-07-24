import html_resumo_de_poltrona_de_trecho_IMP

def gera(pol, id_trc, alterar_pol, comprar_pol, trocar_pol, ver_oferta_pol,
         ver_fez_checkin, realizar_checkin, id_cpr):
  """Devolve uma lista de fragmentos HTML que decrevem a poltrona {pol},
  um objeto da classe {Objeto_Poltrona}.  A poltrona deve pertencer ao
  trecho {id_trc}.  A lista terá um elemento string separado
  para cada campo ou botão.  Esta tupla deve ser usada como uma linha do
  argumento de {html_table}.

  A linha sempre terá os seguintes elementos: número da poltrona, o
  identificador do pedido de compra para o qual foi reservado (p. ex.
  "C-00002322" ou "LIVRE"), o preço, uma indicação se a poltrona está em
  oferta, e um botão "Ver".
  
  Quando o botão "Ver" for clicado, ele emite of comando HTTP
  "ver_poltrona", com o identificador {id_pol} da poltrona no 
  parâmetro 'id_poltrona'.

  Se {alterar_pol} for {True}, a função supõe que o dono da sessão
  corrente pode alterar os atributos da poltrona, como preço e condição
  de oferta. (Só deveria ser {True} se o dono da sessão for um
  administrador.) Nesse caso a linha terá um botão "Alterar" que, quando
  clicado, emitirá o comando HTTP "solicitar_pag_alterar_poltrona", com
  {id_pol} no parâmetro 'id_poltrona'. Caso contrário
  esse botão será omitido.

  Se {comprar_pol} for {True} e a poltrona estiver livre, a linha terá
  um botão "Comprar" que, quando clicado, emitirá o comando HTTP
  "comprar_poltrona", com parâmetros {'id_poltrona': id_pol} e
  {'id_compra': id_cpr}. (Normalmente, este argumento só deveria ser
  {True} se o dono da sessão corrente for um cliente comum, e ele for o
  dono do pedido de compra {id_cpr}, e este pedido estiver em aberto, e
  nenhuma poltrona do mesmo trecho estiver reservada para essa compra.)
  
  Se {trocar_pol} for true, e a poltrona já estiver reservada para a
  compra {id_cpr}, em vez do botão "Comprar" haverá um botão "Trocar"
  que, quando clicado, emite o comando "trocar_poltrona" com parãmetro
  {'id_poltrona': id_pol}. (Normalmente, este argumento só deveria ser
  {True} se o dono da sessão corrente for um cliente comum, e ele for o
  dono do pedido de compra {id_cpr}, e este pedido estiver em aberto.
  Portanto {comprar_pol} e {trocar_pol} não podem ser ambos {True}.)"""
  return html_resumo_de_poltrona_de_trecho_IMP.gera \
    (pol, id_trc, alterar_pol, comprar_pol, trocar_pol, ver_oferta_pol,
         ver_fez_checkin, realizar_checkin, id_cpr)
