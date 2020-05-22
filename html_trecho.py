import html_trecho_IMP

def gera(ses, trc, detalhe):
  """Retorna um trecho HTML que descreve um trecho de viagem {trc}.
  
  Se {detalhe} é {False}, o resultado é uma tupla fragmentos HTML que são campos para uma linha 
  de uma tabela HTML (vide {html_tabela.gera}), contendo os atributos do trecho.
  
  Se {detalhe} é {True}, o resultado é um único bloco texto contendo os atributos do trecho,
  seguido da lista de poltronas {pols} do mesmo, gerada por 
  {html_lista_de_poltronas.gera(ses, pols)}."""
  return html_trecho_IMP.gera(ses, trc, detalhe)
