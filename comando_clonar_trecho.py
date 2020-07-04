# Este módulo processa o acionamento do botão "clonar Trecho" dentro
# do formulário com os dados para clonar trecho da página {solicitar_pag_clonar_trecho}. 
# Ele é acionado através do usuário Administrador.

import comando_clonar_trecho_IMP

def processa(ses, args):
  """Esta função é chamada quando o administrador aperta o botão "clonar Trecho"
  em um formulário para Clonar um trecho, copiando os campos do mesmo para um novo.
  
  Os dados do trecho devem estar definidos no dicionário {args}.
  
  Se os dados forem aceitáveis, a função acrescenta o trecho,
  à base de dado.
  
  Se os dados não forem aceitáveis, a função devolve o
  mesmo formulário de clonar trecho, com os mesmos
  dados nos campos preenchidos, com uma ou mais mensagens de erro
  adequadas."""
  return comando_clonar_trecho_IMP.processa(ses, args)
