import comando_solicitar_pag_alterar_poltrona_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Alterar"
  na página que lista as poltronas.  
  
  A função retorna uma página HTML {pag} com o formulário que mostra os
  dados de uma certa poltrona {pol}, com campos editáveis.
  O formulário deve conter um botão de submissão "Alterar".
  
  O argumento {ses} deve ser uma sessão atualmente aberta.
  
  O dicionário de argumentos {args} pode ser vazio ou conter um único 
  campo com chave "id_poltrona". 
  
  Se o campo {args["id_poltrona"]} não existir ou for {None},
  o formulário retorna um erro de poltrona não identificada.
  
  Se o campo {args["id_poltrona"]} existir e não
  for {None}, o formulário vai mostrar os dados da poltrona {pol}
  cujo identificador é {args["id_poltrona"]}."""
  return comando_solicitar_pag_alterar_poltrona_IMP.processa(ses, args)
