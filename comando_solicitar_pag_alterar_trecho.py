import comando_solicitar_pag_alterar_trecho_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Alterar"
  em alguma linha ou página referente a um determinado trecho {trc}.  
  
  O argumento {ses} deve ser uma sessão atualmente aberta,
  e o dono deve ser um administrador.
  
  O dicionário de argumentos {args} deve conter um 
  campo com chave 'id_trecho' cujo valor é o identificador do
  trecho {trc} a alterar.
  
  Em caso de sucesso, a função retorna uma página HTML {pag} com o formulário que mostra os
  dados do trecho {trc}, com campos editáveis. O formulário vai conter
  um botão de submissão "Alterar" e um botão "Clonar".
  
  Em caso de erro, o resultado é uma pagina com a mensagem de erro."""
  return comando_solicitar_pag_alterar_trecho_IMP.processa(ses, args)

