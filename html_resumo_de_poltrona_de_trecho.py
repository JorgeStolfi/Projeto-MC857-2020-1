import html_resumo_de_poltrona_de_trecho_IMP

def gera(pol, alterar, comprar, excluir, fazer_checkin):
  """Devolve uma lista de fragmentos HTML que decrevem a poltrona {pol},
  que deve ser um objeto da classe {Objeto_Poltrona}. A lista terá um
  elemento string separado para cada campo ou botão. Esta tupla deve ser
  usada como uma linha do argumento de {html_table}.

  A linha sempre terá as seguintes colunas: número da poltrona, o preço,
  uma indicação se a poltrona está em oferta, o identificador do pedido
  de compra para o qual o assento foi reservado (p. ex. "C-00002322" ou
  "LIVRE"), uma indicação de se o passageiro já fez checkin, um botão
  "Ver", e um botão de ação. 
  
  Se {alterar}, {comprar}, ou {excluir} for {True}, o botão
  de ação será "Alterar", "Comprar" ou "Excluir", respectivamente.  No
  máximo um desses três parâmetros pode ser {True}; se os três forem {False},
  essa coluna será deixada em brsnco. 
  
  Quando clicado, o botão "Ver" emitirá o comando HTTP "ver_poltrona". O
  botão "Alterar" emitirá o comando "solicitar_pag_alterar_poltrona"; o
  botão "Comprar" emitirá "comprar_poltrona"; e o botão "Excluir" emtirá
  "excluir_poltrona".
  
  O parâmetro {fazer_checkin} solicita a inclusão de três colunas
  adicionais: o nome do passageiro para o qual esta poltrona foi
  reservada, seu documento, e um botão "Checkin" que, quando clicado,
  emite o comando "fazer_checkin". Estas tres colunas estarão em branco
  se a poltrona estiver livre. O botão "Checkin" só deve existr se o
  passageiro ainda não fez checkin. 
  
  Todos os comandos emitidos pelos botões terão argumento {'id_poltrona': id_pol}.
  
  Observações sobre uso esperado:
  
  O parâmetro {alterar} deveria ser {True} se o dono da sessão for
  um administrador, e {False} se o usuário não estiver logado, ou o dono
  da sessão for um cliente comum. 
  
  Se {alterar} for {False}, a poltrona deve estar
  livre ou atribuída a esse cliente, pois um usuário não logado ou um
  cliente comum não precisa ver poltronas reservadas para outros
  usuários. 
  
  Além disso, se {comprar} for {True}, o usuário deveria
  estar logado, esta poltrona deveria estar livre, o trecho não pode
  estar encerrado, e os horários deste trecho deveriam ser compatíveis
  com as poltronas já incluídas no carrinho de compras desse cliente. 
  
  Se {excluir} for true, o usuário deveria estar logado, esta poltrona
  devira estar reservada para uma compra do cliente, essa compra deveria
  ainda ainda estiver em aberto, e este trecho não pode estar.)
  
  Se {fazer_checkin} for {True}, {alterar_pol} deveria ser {True}.)"""
  return html_resumo_de_poltrona_de_trecho_IMP.gera(pol, alterar, comprar, excluir, fazer_checkin)

def gera_cabecalho(fazer_checkin):
  """Devolve uma lista com os cabeçalhos para as colunas
  produzidas por {gera} com estilo adequado."""
  return html_resumo_de_poltrona_de_trecho_IMP.gera_cabecalho(fazer_checkin)

def gera_legenda(fazer_checkin):
  """Devolve uma legenda explicando cabeçalhos e valores, se necessario, para ser
  colocada abaixo da tabela."""
  return html_resumo_de_poltrona_de_trecho_IMP.gera_legenda(fazer_checkin)
