
import html_lista_de_poltronas_IMP

def gera(ses, cpr, tre, ids):
  """Retorna um trecho de HTML que descreve as poltronas cujos identificadores
  estão na lista {ids}.  
  
  Se {cpr} não é {None}, todas as poltronas devem pertencer ao pedido de compra compra {cpr}. 
  Nesse caso mostra botão "Excluir" para excluir a poltrona da compra e {tre} deve ser {None}. 
  
  Se {tre} não é {None}, todas as poltronas devem pertencer ao trecho {tre}.
  
  Em qualquer caso, será monstrado um botão {Ver}, que, quando clicado,
  devolve uma página com os dados detalhados da poltrona."""
  return html_lista_de_poltronas_IMP.gera(ses, cpr, tre, ids)
