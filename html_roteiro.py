
import html_roteiro_IMP

def gera(ses, rot, detalhe):
  """Devolve um fragmento HTML que descreve um roteiro consistindo de 
  um ou mais trechos (vide {roteiro.py}). 
  
  A descrição tem um cabeçalho com os dados do resumo do roteiro,
  obtidos por {roteiro.obtem_resumo(rot)} e formatados por
  {html_resumo_de_roteiro.gera(ses, res)}.  
  
  Se {detalhe} for {True}, são mostrados em seguida os dados de cada
  trecho, com {html_lista_de_trechos.gera(ses, rot)}."""
  return html_roteiro_IMP.gera(ses, rot, detalhe)
  
