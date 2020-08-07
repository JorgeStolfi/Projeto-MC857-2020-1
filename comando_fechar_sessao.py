# Este módulo processa o acionamento do botão "Fechar sessão" de uma página de "ver sessão". 

import comando_fechar_sessao_IMP

def processa(ses, args):
  """Esta função é chamada quando um administrador aperta o botão "Fechar sessão"
  durante a visualização de um objeto sessão.
  
  A sessão {ses} não pode ser {None}, e deve estar aberta. O dicionário
  {args} deve conter o campo 'id_sessao' com o ID da sessão a ser fechada.
  
  A função fecha a sessão cujo ID é args['id_sessao'] e retorna o HTML da página 
  principal (homepage) da loja. 
  
  Caso a sessão a ser fechada seja a sessão atual do usuário,
  equivale a fazer logout.

  ATENÇÃO: este comando retors dois resultados, {pag, ses_nova};  onde
  {pag} é a página a exibir, e {ses_nova} é {None} se a sessão {ses} foi
  fechada, senão é a própria {ses}.
  """
  return comando_fechar_sessao_IMP.processa(ses, args)
