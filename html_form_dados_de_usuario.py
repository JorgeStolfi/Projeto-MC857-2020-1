import html_form_dados_de_usuario_IMP

def gera(id_usuario, atrs, admin, texto_bt, comando_bt):
  """Retorna um formulário para cadastrar ou alterar os dados de um usuário.
  
  Os campos do formulário serão inicializados com os atributos 
  no dicionário {atrs} (e não com os atributos atuais do usuário).
  
  Se o parâmetro booleano {admin} for {True}, a função supõe que o formulário 
  foi solicitado por um administrador.  Nesse caso o formulário mostrará o 
  atributo 'administrador' como editável.
  
  Se {id_usuario} é {None}, retorna formulário de cadastrar novo usuário.
  Não haverá um campo para o dentifcador, e todos os campos serão editáveis.  
  
  Se {id_usuário} não é {None}, retorma o formulário para alterar os dados 
  do usuário {usr} cujo identificador é {id_usuario}, que supostamente já
  existe.  O identificador será visível se {admin} for {True}.
  Todos os campos serão editáveis, exceto 'identificador', 'email', e 'CPF'.  
  
  Em qualquer caso, o formulário terá um campo adicional 'conf_senha'.

  O formulário terá um botão de tipo "submit" com texto {texto_bt} que, quando ativado,
  gera uma ação POST comando {comando_bt}.  Haverá também um botão simples com texto 
  "Cancelar" que emite o comando "principal". """
  return html_form_dados_de_usuario_IMP.gera(id_usuario, atrs, admin, texto_bt, comando_bt)
