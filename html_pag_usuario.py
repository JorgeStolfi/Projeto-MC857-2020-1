import html_pag_usuario_IMP

def gera(ses, usr, atrs, erros):
  """Retorna uma página HTML que mostra os dados do usuário {usr},
  para visualização, alteração, ou criação de novo usuário.

  Caso {atrs} não seja {None}, deve ser um dicionário que (re)define
  valores para alguns ou todos os atributos de um {Objeto_Usuario}. Se
  um atributo for definido em {atrs}, mesmo como {None}, o valor
  correspondente tem precedência sobre o valor em {usr}.
  
  O parâmetro {ses} é a sessão que pediu esta página, que pode ser
  {None} se o usuário não está logado. O parâmetro {erros} é uma lista
  de mensagens de erro a mostrar no alto da página. Pode ser {None}.
  
  A página conterá um <form>...</form> com campos <input> para os
  atributos do usuário. Vide detalhes em
  {html_form_dados_de_usuario.gera}. Os campos e botões que aparecem na
  página dependem do caso determinado por {ses} e {usr}.

    Se {usr} for {None}, entende-se que o propósito da página é a criação
    (cadastramento) de um novo usuário.  Nesse caso {ses} pode ser qualquer sessão,
    ou {None} (se o usuário não fez login).  Haverá um botão "Cadastrar"
    para confirmar a criação.

    Se {usr} não for {None}, entende-se que o usuário {usr} está sendo
    visualizado e possivelmente alterado. Neste caso, {ses} não pode
    ser {None}, e deve ser uma sessão de administrador ou do próprio {usr}. Se
    {ses} for de administrador, o formulário incluirá um campo
    visível 'id_usuario' com o ID de {usr}, como "readonly"; caso
    contrário esse campo será "hidden". Haverá um botão "Alterar" para
    confirmar as alterações.

  Em qualquer caso, se {ses} for sessão de administrador, o formulário
  incluirá o campo 'administrador' de {usr} como um checkbox visível. Caso
  contrário esse campo será omitido.

  Em qualquer caso, o valor do atributo 'senha' será deixado em branco,
  e haverá um campo adicional no formulário 'conf_senha'.

  A página também terá um botão simples "Cancelar" ou "Voltar",
  que, quando clicado, emite o comando "principal".

  """
  return html_pag_usuario_IMP.gera(ses, usr, atrs, erros)
