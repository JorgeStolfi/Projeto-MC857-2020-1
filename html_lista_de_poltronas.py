
import html_lista_de_poltronas_IMP

def gera(ses, cpr, trc, ids, excluir):
  """Retorna um trecho de HTML que descreve as poltronas cujos identificadores
  estão na lista {ids}.  
  
  Se {cpr} não é {None}, todas as poltronas devem pertencer ao pedido de compra compra {cpr}. 
  Nesse caso {trc} deve ser {None} e {comprar} e {alterar} devem ser {False}.
  Ale disso, se {excluir} for {True},
  a compra deve estar em aberto, e cada poltrona terá um botão "Excluir"
  que, quando clicado, emitirá o comando HTTP "excluir_poltrona", com o
  identificador da potrona como argumento. 
  
  Se {trc} não é {None}, todas as poltronas devem pertencer ao trecho {trc}.
  Nesse caso {excluir} deve ser {False}.
  
  Em qualquer caso, será monstrado um botão "Ver", que, quando clicado,
  emite of comando HTTP "ver_poltrona", com o identificador de poltrona como argumento."""
  return html_lista_de_poltronas_IMP.gera(ses, cpr, trc, ids, excluir)
