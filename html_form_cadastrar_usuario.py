import html_form_cadastrar_usuario_IMP

def gera(atrs, admin):
  """Retorna o formulário de cadastrar novo usuario.

  O formuláro contém campos editáveis para as informações que o usuário
  deve preencher.  Se {atrs} não for {None}, deve ser um dicionário
  que define os valores iniciais dos campos.

  O parâmetro {admin} diz que o usuário que pediu a criação do usuário
  (NÃO o usuário que está sendo cadastrado!) é administrador. Se for {True}, o
  formulário vai mostrar um checkbox para definir o novo usuário como
  administrador.

  O formulário conterá um botão 'Cadastrar' (de tipo 'submit').
  Quando o usuário clicar nesse botão, será emitido um comando POST com ação
  {cadastrar_usuario}.  Os argumentos desse POST são todos os atributos da classe {ObjUsuario},
  com os valores de {atrs} que o usuário deve ter preenchido.  Um argumento
  adicional 'conf_senha' conterá a confirmação de senha.

  O formulário também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'principal'."""
  return html_form_cadastrar_usuario_IMP.gera(atrs, admin)
