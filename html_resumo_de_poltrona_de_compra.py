import html_resumo_de_poltrona_de_compra_IMP

def gera(pol, id_compra, ver, excluir):
  """Devolve um fragmento HTML que decreve a poltrona {pol}, 
  um objeto da classe {Objeto_Poltrona}.  A poltrona deve ser
  parte de um pedido de compra com identificador {id_compra}.
  
  O fragmento mostra os dados essenciais do trecho ao qual a poltrona
  pertence (identificador "T-{NNNNNNNN}", código do voo, porto, dia, e hora de 
  partida e chegada), o número da poltrona, e o preço.
 
  Se {excluir} for {True}, a linha terá um botão "Excluir" que, quando
  clicado, emitirá o comando HTTP "excluir_poltrona" com argumentos
  {'id_poltrona': id_poltrona, 'id_compra': id_compra}. (Normalmente,
  este botão só deveria ser solicitado se o pedido de compra ainda estiver em aberto,
  Além disso, o dono da sessão corrente deveria ser um administrador,
  ou um cliente comum que é o dono do pedido de compra.) 
  
  Em qualquer caso, será monstrado um botão "Ver", que, quando clicado,
  emite of comando HTTP "ver_poltrona", com 
  argumento {'id_poltrona': id_poltrona}.
   
  O resultado não é um string, mas uma tupla com um string separado 
  para cada campo ou botão.  Esta tupla deve ser usada como uma linha do
  argumento de {html_table}."""
  return html_resumo_de_poltrona_de_compra_IMP.gera(pol, id_compra, ver, excluir)
