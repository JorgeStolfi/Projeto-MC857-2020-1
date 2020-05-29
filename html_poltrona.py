import html_poltrona_IMP

def gera(ses, pol, ver, excluir):
  """Devolve um fragmento HTML que decreve a poltrona {pol}, 
  um objeto da classe {Objeto_Poltrona}.
  
  O fragmento mostra o identificador do trecho (p .ex. "T-00002311"), o número da poltrona,
  o identificador do pedido de compra para o qual foi reservado (p. ex. "C-00002322"
  ou "LIVRE"), e o preço.
  
  Se a poltrona está livre e for uma oferta, mostra uma indicação desse fato.
  
  Se a poltrona está livre e a sessão {ses} não for {None} e estiver aberta, gera também 
  um botão "Comprar" cujos parâmetros são o identificador da poltrona (p. ex. "A-00023441")
  e o  identificador do pedido de compra que é o carrinho da sessão {ses} (p. ex. "C-00000333").
  
  O resultado não é um string, mas uma tupla com um string separado 
  para cada campo ou botão.  Esta tupla deve ser usada como uma linha do
  argumento de {html_tabela}.
  
  Se {ver} for {True} coloca um botão "Ver" com comando "ver_poltrona".
 
  Se {excluir} for {True} coloca um botão "Excluir" com comando "excluir_poltrona"."""
  return html_poltrona_IMP.gera(pol, ver, excluir)
