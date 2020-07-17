import comando_buscar_trechos_IMP


def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Buscar" em um
  formulário de busca de trecho (vide {html_pag_buscar_trechos.gera}).

  O parâmetro {args} é um dicionário que contém um subconjunto dos
  atributos de um {Objeto_Trecho} (vide {trecho.py}).  Por exemplo,
  {{'origem': "SDU", 'dia_chegada': "2020-05-08"}}.  Campos de {args}
  com valor {None} devem ser ignorados.  A função
  deve procurar na base de dados todos os trechos que possuem
  esse valores nessas colunas.

  Caso pelo menos um atributo correspondentes às chaves {'dia_chegada', 'dia_partida'}
  esteja definido, os trechos seram filtrados pelo valor deste atributo. Estando um destes
  atributos definido e adicionalmente, os atributos correspondentes à {'hora_chegada', 'hora_partida'}
  estiverem definidos, estes também serão utilizados como critério para o filtro de trechos.

  O resultado deve ser uma página com a lista de todos os trechos
  encontrados, gerada por {html_pag_lista_de_trechos.gera}."""
  return comando_buscar_trechos_IMP.processa(ses, args)
