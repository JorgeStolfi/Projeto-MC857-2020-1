import comando_buscar_compras_IMP


def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Buscar" em um
  formulário de busca de compra (vide {html_pag_buscar_compras.gera}).

  O parâmetro {args} é um dicionário que contém um subconjunto dos
  atributos de um {Objeto_Compra} (vide {compra.py}).  Por exemplo,
  {{'cliente': "U-000001", 'status': "pendente"}}.  Campos de {args}
  com valor {None} devem ser ignorados.  A função
  deve procurar na base de dados todas as compras que possuem
  esse valores nessas colunas.

  O resultado deve ser uma página com a lista de todas as compras
  encontradas, gerada por {html_pag_lista_de_compras.gera}."""
  return comando_buscar_compras_IMP.processa(ses, args)
