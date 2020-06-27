import comando_buscar_usuario_IMP


def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Buscar" em um
  formulário de busca de usuario (vide {html_pag_buscar_usuarios.gera}).

  O parâmetro {args} é um dicionário que contém um subconjunto dos
  atributos de um {Objeto_usuario} (vide {usuario.py}).  Por exemplo,
  {{'nome': "João", 'email': "joao@email.com"}}.  Campos de {args}
  com valor {None} devem ser ignorados. O campo {args} deve pelos menos conter
  um dos seguintes atributos de usuário: {'email'} ou {'CPF'}. A função
  deve procurar na base de dados o usuário correspondente.

  O resultado deve ser uma página com o usuário encontrado, gerada
  por {html_pag_lista_de_usuarios.gera}."""
  return comando_buscar_usuario_IMP.processa(ses, args)
