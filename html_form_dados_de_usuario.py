import html_form_dados_de_usuario_IMP

def gera(id_usr, atrs, admin, ht_submit):
  """Retorna um <form>...</form> com os dados do usuário
  cijo identificador é {id_usr}, que pode ser {None}
  no caso de um trecho que está sendo criado.
  
  O formuláro vai conter campos com os atributos de um {Objeto_Usuario},
  cujos valores serão inicializados com os atributos no dicionário
  {atrs} (e NÃO com os atributos atuais do usuário).
  
  Se o parâmetro booleano {admin} for {True}, a função supõe que o
  formulário foi solicitado por um administrador. Nesse caso o
  formulário mostrará o atributo 'administrador' como editável. Caso
  contrário, esse campo será omitido.

    Se {id_usr} é {None}, retorna um formulário apropriado para
    cadastrar novo usuário. Não haverá um campo para o identificador, e
    todos os campos serão editáveis. Neste caso, {admin} pode ser
    {False}, pois o cadastramento pode ser feito por qualquer usuário,
    mesmo sem dar login.

    Se {id_usr} não é {None}, retorma um formulário apropriado para
    visualizar ou alterar os dados do usuário {usr} cujo identificador é
    {id_usr}, que supostamente já existe. Neste caso, {admin} pode ser
    {False}; mas a a função supõe que quem pediu o formulário é esse
    mesmo usuário. Todos os campos serão editáveis, exceto
    'identificador', 'email', e 'CPF'. O identificador será visível
    somente se {admin} for {True}.

  Em qualquer caso, o formulário terá um campo adicional 'conf_senha'.
  Esse campo e o campo 'senha' serão deixados em branco, mesmo que
  constem de {atrs}.

  O parâmetro {ht_submit}, se não for {None}, deve ser o HTML que será
  incluído no <form>...</form> após todos os campos. Deve conter pelo
  menos um botão de tipo "submit". Quando acionado, esse botão vai
  causar a emissão de um comando HTTP "POST" com os dados do formulário.

  """
  return html_form_dados_de_usuario_IMP.gera(id_usr, atrs, admin, ht_submit)
