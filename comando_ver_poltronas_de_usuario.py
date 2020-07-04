import comando_ver_poltronas_de_usuario_IMP

def processa(ses, args):
  """Esta função é chamada quando um usuário aperta o botão "Ver Poltronas"
  quando pesquisa um objeto através do "Checar Objeto". 
  
  A sessão corrente {ses} não pode ser {None} e deve estar aberta.

  A função retorna uma página HTML {pag} contendo todas as poltronas associadas as compras
  do usuário pesquisado."""
  
  return comando_ver_poltronas_de_usuario_IMP.processa(ses, args)

