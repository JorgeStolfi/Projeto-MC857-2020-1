# Este módulo processa o acionamento do botão "Contato" do menu principla pelo usuário.

import comando_solicitar_pag_contato_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Contato" 
  no menu geral de uma página qualquer.  
  
  A sessão corrente {ses} e o dicionário de argumentos {args}
  são irrelevantes e podem ser {None}.
  
  A função retorna a página HTML {pag}, com o telefone de contato."""
  return comando_solicitar_pag_contato_IMP.processa(ses, args)

