
import html_lista_de_roteiros_IMP

def gera(ses, rots):
  """Devolve um trecho de HTML que descreve uma lista de roteiros {rots}.
  
  Cada roteiro {rot} em {rots} será formatado por {html_resumo_de_roteiro.gera}.
  Terá um botão "Ver" para examinar detalhes do roteiro.  """
  return html_lista_de_roteiros_IMP.gera(ses, rots)
