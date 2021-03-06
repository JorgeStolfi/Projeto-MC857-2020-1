import comando_ver_compra_IMP

def processa(ses, args):
  """Esta função é chamada quando um usuário aperta o botão "Ver"
  numa lista de compras. 
  
  A sessão corrente {ses} não pode ser {None} e deve estar aberta.

  A função retorna uma página HTML {pag} contendo os dados da compra
  cujo identificador é o valor de {args['id_compra']}. 
  
  A lista de bilhetes (poltronas, trechos) também é mostrada.
  Se a compra pertence ao usuário que é dono da sessão {ses},
  ou este último for um administrador, haverá um bootão "Excluir"
  em cada poltrona, que, quando pressonado, gera o comando 
  "excluir_poltrona_de_compra" com o identificador da poltrona
  como argumento."""
  return comando_ver_compra_IMP.processa(ses, args)
