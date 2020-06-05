import html_pag_criar_roteiro_IMP

def gera(ses, erros):
  """Retorna uma página contendo o formulário de criar roteiro.
  O formulário tem campos editáveis para especificar 
  portos de origem e destino, dia mínimo de partida de 
  dia máximo de chegada, etc.
  
  O formulário contém um botão com texto "Pesquisar" que, quando 
  acionado, emite uma ação POST com comando 'criar_roteiro'."""
  return html_pag_criar_roteiro_IMP.gera(ses, erros)
