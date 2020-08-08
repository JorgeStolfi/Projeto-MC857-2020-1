
import html_lista_de_poltronas_de_trecho_IMP

def gera(ids_poltronas, usr, carr):
  """Retorna um trecho de HTML que descreve as poltronas cujos identificadores
  estão na lista {ids_poltronas}.  Todas as poltronas devem pertencer ao 
  mesmo trecho, que supõe-se ter sido identificado separadamente.
  
  O resultado é um elemento "<table>...</table>" seguido possivelmente de uma
  legenda. 
  
  O parâmetro {usr} deve ser o identificador do dono da sessão corrente,
  ou {None} se ele não está  logado.  O parâmetro {carr} deve ser o identificador 
  do carrinho de compras dessa sessão carrinho, ou {None} se ele não está logado
  ou é administrador.
  
  Cada linha da tabela é gerada por
  {html_resumo_de_poltrona_de_trecho.gera} com argumentos {(pol,
  alterar, comprar, excluir, fazer_checkin, embarcar)}. O parâmetro {alterar} será
  {True} se e somente se {usr} for administrador. O parãmetro {comprar}
  será {True} se e somente se {usr} não for nem {None} nem
  administrador, a poltrona {pol} estiver livre, não houver impedimento
  ao usuário comprar essa poltrona (por exemplo, o trecho 
  foi encerrado, a compra {carr} já inclui alguma poltrona desse ou
  outro trecho com horários conflitantes.) O parâmetro {excluir} será
  {True} se a poltrona estiver atribuída a alguma compra do usuário
  {usr} e não houver impedimento para excluir essa poltrona (por
  exemplo, o trecho foi encerrado).

  """
  return html_lista_de_poltronas_de_trecho_IMP.gera(ids_poltronas, usr, carr)
