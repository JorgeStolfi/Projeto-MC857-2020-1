import html_form_alterar_trecho_IMP

def gera(id_trecho, atrs, admin):
  """Retorna o formulário de alterar dados do trecho {trc}
  cujo identificador é {id_trecho}.

  O formulário contém campos editáveis com os atributos
  correntes do trecho, especificados no dicionário {atrs}.
  O valor de {atrs['senha']} não será mostrado, e haverá um
  campo adicional 'conf_senha'.

  O parâmetro {admin} diz que o usuário que pediu a alteração é administrador.
  Se for {True}, o formulário vai mostrar todos os campos como editáveis, menos o
  atributo código, que será mostrado como "readonly".

  Se {admin} for {False}, supõe-se que o formulário foi
  pedido pelo próprio {usr}, que é um cliente comum, portanto, não podendo
  editar nenhum campo, portanto, não podendo
  editar nenhum campo.

  O formulário conterá um botão 'Alterar' (de tipo 'submit').
  Quando o usuário clicar nesse botão, será emitido um comando POST com ação
  {alterar_trecho}.  Os argumentos desse POST são todos os atributos da classe
  {Objeto_Trecho}, com os valores de {atrs} a menos de alterações feitas pelo
  usuário, mais o atributo 'conf_senha'.

  O formulário também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'principal'."""
  return html_form_alterar_trecho_IMP.gera(id_trecho, atrs, admin)
