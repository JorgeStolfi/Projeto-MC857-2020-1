
import html_form_acrescentar_trecho_IMP

def gera(atrs):
  """Retorna um formulário HTML ("<form>....</form>") que permite ao administrador especificar
  um trecho (uma viagem de um veículo em uma determinada data, entre duas escalas)
  a ser acrescentado à tabela de trechos.  O formuláro contém campos
  editáveis para as colunas dessa tabela, como código do voo, códigos dos
  aeroportos de origem e destino, datas e horários, etc.
  
  O parâmetro {atrs} é um dicionário que contém valores iniciais para 
  alguns ou todos esses campos. Pode ser vazio.

  O formulário conterá um botão 'Acrescentar' (de tipo 'submit').
  Quando o administrador clicar nesse botão, será emitido um comando POST com ação
  {acrescentar_trecho}.  Os argumentos desse POST são todos os atributos da classe 
  {Objeto_Trecho} que o administrador deve ter preenchido.

  O formulário também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'principal'."""
  return html_form_acrescentar_trecho_IMP.gera(atrs)

