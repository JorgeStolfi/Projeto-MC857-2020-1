import html_pag_alterar_trecho_IMP

def gera(ses, id_trecho, atrs, erros, clonar):
  """Retorna uma página com formulário para alterar os dados
  do trecho {trc} cujo identificador é {id_trecho}.
  Normalmente esta página é criada para um administrador do site.
  
  A página contém campos editáveis para entrar os novos atributos do
  trecho.  Os valores desses campos são inicializados com os valores
  especificados no dicionário {atrs} (e NÃO com os atributos atuais do trecho).

  Vide detalhes em {html_form_dados_de_trecho.gera}.
  
  Caso clonar seja True, cria um novo trecho em vez de alterar o atual."""
  if clonar == None:
    clonar = False
  return html_pag_alterar_trecho_IMP.gera(ses, id_trecho, atrs, erros, clonar)
