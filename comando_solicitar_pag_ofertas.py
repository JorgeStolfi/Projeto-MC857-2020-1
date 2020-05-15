# Este módulo processa o acionamento do botão "Ofertas" do menu principal pelo usuário.

import comando_solicitar_pag_ofertas_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Ofertas"
  no menu geral de uma página qualquer.  
  
  A sessão corrente {ses} e o dicionário de argumentos {args}
  são irrelevantes e podem ser {None}, por ora.
  Podem se tornar relevantes para filtros ou ofertas direcionadas
  aa usuários específicos.
  
  A função retorna a página HTML {pag}, com a lista de ofertas a serem
  exibidas ao usuário."""
  return comando_solicitar_pag_ofertas_IMP.processa(ses, args)

