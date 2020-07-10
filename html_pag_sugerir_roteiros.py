import html_pag_sugerir_roteiros_IMP

def gera(ses, erros):
  """Retorna uma página contendo o formulário de criar roteiro.
  O formulário tem campos editáveis para especificar 
  portos de origem e destino, dia mínimo de partida de 
  dia máximo de chegada, etc.
  
  O formulário contém um botão com texto "Pesquisar" que, quando 
  acionado, emite uma ação POST com comando 'sugerir_roteiros'."""
  return html_pag_sugerir_roteiros_IMP.gera(ses, erros)
