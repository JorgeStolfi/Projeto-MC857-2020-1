import comando_solicitar_pag_alterar_trecho_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Alterar"
  na página que lista os trechos.  
  
  A função retorna uma página HTML {pag} com o formulário que mostra os
  dados de um certo trecho {trc}, com campos editáveis.
  O formulário deve conter um botão de submissão "Alterar".
  
  O argumento {ses} deve ser uma sessão atualmente aberta.
  
  O dicionário de argumentos {args} pode ser vazio ou conter um único 
  campo com chave "id_trecho". 
  
  Se o campo {args["id_trecho"]} não existir ou for {None},
  o formulário retorna um erro de trecho não identificado.
  
  Se o campo {args["id_trecho"]} existir e não
  for {None}, o formulário vai mostrar os dados do trecho {trc}
  cujo identificador é {args["id_trecho"]}."""
  return comando_solicitar_pag_alterar_trecho_IMP.processa(ses, args)

