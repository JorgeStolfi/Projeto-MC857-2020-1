import html_form_dados_de_trecho_IMP

def gera(id_trecho, atrs, texto_bt, comando_bt):
  """Retorna um <form>...</form> com os dados do {trecho}
   cujo identificador é {id_trecho}.

  O formuláro contém campos editáveis com os atributos
  de um trecho, cujos valores são inicializados conforme o dicionário
  {atrs} (e NÃO com os atributos correntes do trecho). 

  O formulário conterá um botão (de tipo 'submit') com texto {texto_bt}
  que, quando acionado, emite uma ação POST com comando {comando_bt}. Os
  argumentos desse POST são todos os atributos da classe
  {Objeto_Trecho}, com os valores de {atrs} a menos de alterações feitas
  pelo usuário.

  O formulário também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'principal'."""
  return html_form_dados_de_trecho_IMP.gera(id_trecho, atrs, texto_bt, comando_bt)
