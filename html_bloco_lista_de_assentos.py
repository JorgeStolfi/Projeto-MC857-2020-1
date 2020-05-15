
import html_bloco_lista_de_assentos_IMP

def gera(ses, cpr, tre, ids, detalhe):
  """Retorna um trecho de HTML que descreve os assentos cujos identtificadores
  estão na lista {ids}.  
  
  Se {cpr} não é {None}, todos os assentos devem pertencer ao pedido de compra compra {cpr}.
  Nesse caso {tre} deve ser {None}. Se {detalhe} for {True},
  mostra botão "Excluir" para excluir o assento da compra.
  
  Se {tre} não é {None}, todos os assentos devem pertencer ao trecho {tre}.
  
  Em qualquer caso, será monstrado um botão {Ver}, que, quando clicado,
  devolve uma página com os dados detalhados do assento."""
  return html_bloco_lista_de_assentos_IMP.gera(ses, cpr, tre, ids, detalhe)
