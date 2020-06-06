import comando_buscar_usuario_IMP


def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Buscar" em um
  formulário de busca de usuario (vide {html_pag_buscar_usuarios.gera}).

  O parâmetro {args} é um dicionário que contém um subconjunto dos
  atributos de um {Objeto_usuario} (vide {usuario.py}).  Por exemplo,
  {{'origem': "SDU", 'dia_chegada': "2020-05-08"}}.  Campos de {args}
  com valor {None} devem ser ignorados.  A função
  deve procurar na base de dados todos os usuarios que possuem
  esse valores nessas colunas.

  O resultado deve ser uma página com a lista de todos os usuarios
  encontrados, gerada por {html_pag_lista_de_usuarios.gera}."""
  return comando_buscar_usuario_IMP.processa(ses, args)
