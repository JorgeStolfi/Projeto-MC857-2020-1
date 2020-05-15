import html_form_alterar_usuario_IMP

def gera(id_usuario, atrs, admin):
  """Retorna o formulário de alterar dados da conta
  do usuario {usr} cujo identificador é {id_usuario}.

  O formuláro contém campos editáveis com os atributos
  correntes do usuário, especificados no dicionário {atrs}.
  O valor de {atrs['senha']} não será mostrado, e haverá um
  campo adicional 'conf_senha'.

  O parâmetro {admin} diz que o usuário que pediu a alteração (NÃO o
  usuário que está sendo alterado!) é administrador. Se for {True}, o
  formulário vai mostrar um checkbox para definir o usuário {usr} como
  administrador, e vai mostrar também o campo {id_usuario} como "readonly".

  Se {admin} for {False}, supõe-se que o formulário foi
  pedido pelo próprio {usr}, que é um cliente comum. Nesse caso não
  haverá o checkbox "administrador", e o campo {id_usuario} será
  "hidden".

  O formulário conterá um botão 'Alterar' (de tipo 'submit').
  Quando o usuário clicar nesse botão, será emitido um comando POST com ação
  {alterar_usuario}.  Os argumentos desse POST são todos os atributos da classe
  {Objeto_Usuario}, com os valores de {atrs} a menos de altetações feitas pelo
  usuário, mais o atributo 'conf_senha'.

  O formulário também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'principal'."""
  return html_form_alterar_usuario_IMP.gera(id_usuario, atrs, admin)
