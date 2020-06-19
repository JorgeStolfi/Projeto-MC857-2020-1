import html_form_dados_de_compra_IMP

def gera(cpr, admin, texto_bt, comando_bt):
  """Gera um formulário HTML <form>...</form> com os dados principais
  da compra {cpr}, menos a lista de poltronas. Inclui o identificador
  da compra, o preço total, o número de escalas, o porto e data de partida
  do primeiro trecho, o porto e data de chegada do último trecho, o identificador 
  do dono da compra (usuário que a montou ou está montando), o nome do passageiro,
  etc.

  Se {admin} for {False}, supõe que o dono da sessão corrente é o dono da compra.
  O nome do passageiro será editável.  
  
  Se {admin} for {True}, supõe que o dono da sessão corrente é um administrador da
  loja virtual.  Nesse caso mais campos podem ser editáveis."""
  return html_form_dados_de_compra_IMP.gera(cpr, admin, texto_bt, comando_bt)
