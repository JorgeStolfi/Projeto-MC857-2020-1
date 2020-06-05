import html_pag_acrescentar_trecho_IMP

def gera(ses, atrs, erros):
  """Retorna uma página com formulario HTML ("<form>....</form>") 
  que permite a um administrador especificar os dado de um trecho a 
  ser acrescentado à tabela de trechos.  
  
  O formuláro contém campos editáveis para as colunas dessa tabela,
  como código do voo, códigos dos aeroportos de origem e destino,
  datas e horários, etc.  Os valores iniciais a mostrar 
  nos campos do formulário são obtidos do dicionário {atrs},
  que pode ser incompletoou vazio.

  O parâmetro {erros} é uma lista de mensagens de erro a mostrar na página.
  Pode ser {None}.

  O formulário conterá um botão 'Acrescentar' (de tipo 'submit').
  Quando o administrador clicar nesse botão, será emitido uma ação POST com comando
  "acrescentar_trecho".  Os argumentos desse POST são todos os atributos da classe 
  {Objeto_Trecho} que o administrador deve ter preenchido.

  O formulário também terá um botão simples com texto "Cancelar",
  que, quando clicado, emite o comando 'principal'. """
  return html_pag_acrescentar_trecho_IMP.gera(ses, atrs, erros)
