import html_form_dados_de_poltrona_IMP

def gera(id_pol, atrs_pol, alterar, comprar, excluir, id_cpr):
  """Devolve um fragmento HTML "<form>...</form>" que decreve a poltrona
  cujo identificador é {id_pol} e cujos atributos são {atrs_pol}. 
  
  O fragmento contém um elemento <table>...</table>"
  com uma linha para cada atributo da poltrona, incluindo o identificador.

  Se {alterar} for {True}, os atributos que podem ser alterados serão
  campos HTML editáveis, e o formulário terá na parte de baixo um botão
  "Alterar", que causa a submissão ("POST") do formulário com comando
  HTTP "alterar_dados_de_poltrona". Nos argumentos do comando, o
  atributo {'id_compra'} será o valor desse atributo na poltrona {pol},
  que não pode ser alterado mas pode ser {None}. Se {Alterar} for 
  {False}, todos os campos serão "readonly" e não haverá o
  botão de "Alterar".
  
  Se {comprar} for {True}, haverá um botão "Comprar" na parte de baixo,
  que causa a submissão ("POST") do formulário com comando HTTP
  "comprar_poltrona". Nesse caso, a poltrona deve estar livre, e os
  argumentos do comando incluirão o {id_cpr} dado na chave
  'id_compra'.Se {comprar} for {False}, não haverá o botão "Comprar".
  
  Se {excluir} for {True}, haverá um botão "Excluir" na parte de baixo,
  que causa a submissão ("POST") do formulário com comando HTTP
  "excluir_poltrona_da_compra". Nesse caso, a poltrona NÃO deve estar
  livre, mas atribuída à compra cujo identificador é {id_cpr}. Se
  {excluir} for {False}, não haverá o botão "Excluir".
  
  No máximo um dos parâmetros {alterar}, {comprar} e {excluir} deve ser {True}.
  Se {comprar} e {excluir} forem ambos {False}, o parâmetro {id_cpr} 
  deve ser {None}.
  
  Normalmente, se {alterar} for {True}, a sessão corrente deveria pertencer a um administrador do site. 
  Se {comprar} e/ou {excluir} forem {True} a sessão corrente deveria pertencer a um
  usuário comum, e o parâmetro {id_cpr} deveria ser uma das compras abertas do usuário, 
  geralmente o carrinho dessa sessão."""
  return html_form_dados_de_poltrona_IMP.gera(id_pol, atrs_pol, alterar, comprar, excluir, id_cpr)
