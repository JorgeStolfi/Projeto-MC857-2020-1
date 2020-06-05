import html_pag_ver_compra_IMP

def gera(ses, cpr, excluir, trocar, erros):
  """Retorna uma página HTML que mostra os dados do pedido de compra {cpr}
  (que deve ser um objeto de tipo {Objeto_Compra}).
  
  A página terá um cabeçalho com os dados gerais da compra, e em seguida
  a lista das poltronas (bilhetes) da compra.
  
  Se {excluir} for {True}, cada linha terá um botão "Excluir"
  que, quando clicado, emitirá o comando "excluir poltrona"
  como identificador da poltrona como argumento.
  
  Se {trocar} for {True}, cada linha terá um botão "trocar"
  que, quando clicado, emitirá o comando "trocar poltrona"
  como identificador da poltrona como argumento."""
  return html_pag_ver_compra_IMP.gera(ses, cpr, excluir, trocar, erros)
