import comando_solicitar_pag_buscar_trecho_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Buscar Trecho"
  no menu geral de uma página qualquer.
  
  A função retorna uma página HTML {pag} contendo o formulário para definir um
  os atributos da busca, e um botão de sumbissão "Buscar".
  
  O dicionário de argumentos {args} é irrelevantes e pode ser {None}.
  
  A sessão corrente {ses} pode ser {None}."""
  return comando_solicitar_pag_buscar_trecho_IMP.processa(ses, args)

