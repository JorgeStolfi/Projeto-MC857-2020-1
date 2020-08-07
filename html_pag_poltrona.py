import html_pag_poltrona_IMP

def gera(ses, pol, atrs, erros):
  """Retorna uma página HTML que mostra os dados da poltrona {pol}
  (que deve ser um objeto de tipo {Objeto_Poltrona}), para visualização
  e possivelmente alteração dos mesmos.

  Caso {atrs} não seja {None}, deve ser um dicionário que (re)define
  valores para alguns ou todos os atributos de um {Objeto_Poltrona}. Se um
  atributo tiver valor definido em {atrs}, mesmo que {None}, esse
  valor tem precedência sobre o valor em {pol}.
  
  Se o usuário da sessão {ses} for administrador, o identificador da
  poltrona será visível, e alguns campos serão editáveis, incluindo o
  preço e o indicador de "oferta". Haverá um botão "Alterar"
  para confirmar alterações nesses campos. Caso a poltrona esteja
  atribuída a uma compra que ainda está em aberto, haverá um botão
  "Excluir", como descrito abaixo.
  
  Se a sessão {ses} for {None} (usuário nãologado) ou seu dono for um
  cliente comum, todos os atributos da poltrona serão "readonly", e o
  identificado da mesma será "hidden". Porém, se {ses} não for {None},
  poderá haver botões "Comprar", "Excluir", ou "Trocar" para alterar a
  atribuição da poltrona.
  
  Se {excluir} for {True}, {id_compra} deve ser o identificador da
  compra atribuída a essa poltrona. No resultado, haverá um botão
  "Excluir" que emite o comando "excluir_poltrona_de_compra".

  Os botões de submit causam o envio ao servidor, dos dados da poltrona, com as 
  eventuais alterações, por um comando HTTP "POST".  Especificamente:
  
    O botão submit "Alterar" só está presente se o dono da sessão for um administrador,
    e emite o comando "alterar_dados_de_poltrona". 
    
    Os botões "Excluir" e "Trocar" só estarão presentes se a poltrona {pol}
    estiver atribuída a alguma compra, e o dono da sessão for um administrador,
    ou o cliente que é dono dessa compra.  Eles emitirão os comandos
    "excluir_poltrona" e "trocar_poltrona", respectivamente, com 
    o identificador da poltrona como único argumento.
    
    O botão "Comprar" só está presente se a poltrona {pol} estiver
    livre, o trecho da mesma não estiver encerrado, e o dono da
    sessão for um cliente comum. Emitirá o comando "comprar_poltrona",
    com o identificador da poltrona como único argumento.

  A página também terá um botão simples "Cancelar", que, quando clicado, 
  emite o comando 'principal'.

  """
  return html_pag_poltrona_IMP.gera(ses, pol, atrs, erros)
