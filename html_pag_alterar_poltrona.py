import html_pag_alterar_poltrona_IMP

def gera(ses, id_poltrona, atrs, erros):
  """Retorna o formulário de alterar dados da poltrona {pol} 
  cujo identificador é {id_poltrona}.

  O formuláro mostra o identificador {id_poltrona} 
  e um campo para cada atributo da poltrona. Os valores 
  iniciais dos campos são obtidos do dicionáro {atrs}
  (e NÃO dos atrubutos correntes da poltrona).
  
  O identificador {id_poltrona} e os atributos {atrs['id_trecho']} e
  {atrs['numero']} serão apresentados como {readonly}, e os demais como
  editáveis.

  O formulário conterá um botão "Alterar" (de tipo 'submit').
  Quando o usuáro clicar nesse botão, será emitido um comando POST com ação
  {alterar_dados_de_poltrona}.  Os argumentos desse POST são todos os atributos da classe
  {Objeto_Poltrona}, com os valores de {atrs} a menos de altetações feitas pelo
  usuário.

  O formulário também terá um botão simples "Cancelar",
  que, quando clicado, emite o comando 'principal'. """
  return html_pag_alterar_poltrona_IMP.gera(ses, id_poltrona, atrs, erros)
