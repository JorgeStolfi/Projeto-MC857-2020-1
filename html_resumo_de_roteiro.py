import html_resumo_de_roteiro_IMP

def gera(rot, ver):
  """Retorna código HTML que descreve os dados principais do 
  roteiro {rot} (vide {roteiro.py}: aeroportos de origem e destino,
  dia e hora de partida e chegada, número de escalas, e preço total mínimo. 
  Não mostra os trechos individuais.
  
  Se {ver} for {True}, haverá um botão "Ver" que, quandoclicado, emitirá 
  um comando "ver_roteiro".  Nesse comando, o argumento 'roteiro' 
  será um string consistindo dos identificadores de trechos
  separados por vírgulas.
  
  O resultado é uma lista de strings, cada um descrevendo um campo do
  roteiro,num formato adequado para compor uma linha de uma tabela HTML.
  Vide {html_table.gera}. """
  return html_resumo_de_roteiro_IMP.gera(rot, ver)
