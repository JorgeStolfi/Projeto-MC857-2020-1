import comando_buscar_trechos_IMP


def processa(ses, args):
  """Esta função é chamada quando o usuário quer procurar trechos
  com determinadas características.

  O parâmetro {args} é um dicionário que contém um subconjunto dos
  atributos de um {Objeto_Trecho} (vide {trecho.py}).  Por exemplo,
  {{'origem': "SDU", 'dia_chegada': "2020-05-08"}}.  Campos de {args}
  com valor {None} devem ser ignorados.  
  
  O dicionário {args} deve conter pelo menos um dos atributos 'origem' e 'destino',
  e ambos os atributos 'dia_partida' e 'dia_chegada',  Se 'hora_partida' for
  omitida, a função supõe "00:00". Se 'hora_chegada' for
  omitida, a função supõe "23:59".
  
  Se 'origem' for especificada, somente serão retornados 
  trechos com esse aeroporto de origem.  Idem se 'destino' for 
  especificado. Somente serão retornados trechos que partirem 
  em {dia_partida,hora_partida} ou depois, e chegarem
  em {dia_chegada,hora_chegada} ou antes.

  O resultado será uma página com a lista de todos os trechos
  encontrados, gerada por {html_pag_lista_de_trechos.gera}. 
  
  A sessão {ses} pode ser {None}, mas a saída pode ser 
  diferente para administradores, clientes normais, 
  e usuários não logados."""
  return comando_buscar_trechos_IMP.processa(ses, args)
