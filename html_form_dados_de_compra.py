import html_form_dados_de_compra_IMP

def gera(cpr, editavel, texto_bt, comando_bt):
  """Gera um formulário HTML <form>...</form> com os dados principais
  da compra {cpr}, menos a lista de poltronas. Inclui o identificador
  da compra, o preço total, o número de escalas, o porto e data de partida
  do primeiro trecho, o porto e data de chegada do último trecho, o identificador 
  do dono da compra (usuário que a montou ou está montando), o nome do passageiro,
  etc.

  Se {editavel} for {True}, os atributos da compra que podem ser alterados 
  (como o nome do passageiro) serão editáveis.  Nesse caso, haverá
  um botão de "submit" com o texto {texto_bt} que, quando clicado,
  emite um comando POST com ação {comando_bt}, com os valores 
  alterados desses atributos."""
  return html_form_dados_de_compra_IMP.gera(cpr, editavel, texto_bt, comando_bt)
