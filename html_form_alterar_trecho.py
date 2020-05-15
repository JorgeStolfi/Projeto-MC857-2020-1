import html_form_alterar_trecho_IMP

def gera(id_trecho, atrs):
  """Retorna o formulário de alterar dados do {trecho}
   cujo identificador é {id_trecho}.

  O formuláro contém campos editáveis com os atributos
  correntes do trecho, especificados no dicionário {atrs}.

  O formulário conterá um botão 'Alterar' (de tipo 'submit').
  Quando o usuário clicar nesse botão, será emitido um comando POST com ação
  {muda_atributos}.  Os argumentos desse POST são todos os atributos da classe
  {Objeto_Trecho}, com os valores de {atrs} a menos de alterações feitas pelo
  usuário.

  O formulário também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'principal'."""
  return html_form_alterar_trecho_IMP.gera(id_trecho, atrs)
