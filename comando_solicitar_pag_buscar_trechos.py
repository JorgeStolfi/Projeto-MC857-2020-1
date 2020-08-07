import comando_solicitar_pag_buscar_trechos_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário quer buscar trechos segundo 
  certos critérios.
  
  A função retorna uma página HTML {pag} contendo o formulário para definir um
  os argumentos da busca, e um botão de sumbissão "Buscar".
  
  O dicionário de argumentos {args} é irrelevante e pode ser {None}.
  
  A sessão corrente {ses} pode ser {None}."""
  return comando_solicitar_pag_buscar_trechos_IMP.processa(ses, args)

