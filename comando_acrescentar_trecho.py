# Este módulo processa o acionamento do botão "Acrescentar Trecho" dentro
# do formulário com os dados para acrescentar trecho da página {solicitar_pag_acrescentar_trecho}.
# Ele é acionado através do usuário Administrador.

import comando_acrescentar_trecho_IMP

def processa(ses, args):
  """Esta função é chamada quando o administrador aperta o botão "Acrescentar Trecho"
  em um formulário para adicionar um trecho, após ter preenchido os campos do mesmo.

  Os dados do trecho devem estar definidos no dicionário {args}.

  Se os dados forem aceitáveis, a função acrescenta o trecho,
  à base de dado e retorna a página mostrando o trecho criado.

  Se os dados não forem aceitáveis, a função devolve o
  mesmo formulário de acrescentar trecho, com os mesmos
  dados nos campos preenchidos, com uma ou mais mensagens de erro
  adequadas."""
  return comando_acrescentar_trecho_IMP.processa(ses, args)
