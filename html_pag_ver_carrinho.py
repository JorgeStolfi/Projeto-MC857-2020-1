import html_pag_ver_carrinho_IMP


def gera(ses, cpr, erros):
  """Retorna uma página HTML que mostra os dados do carrinho com base em um pedido de compra {cpr}
  (que deve ser um objeto de tipo {Objeto_Compra}).

  A página terá um cabeçalho com os dados gerais da compra, seguida da
  lista das poltronas (bilhetes) da compra com possibilidade de remoção e um botão de finalizar a compra.
  """
  return html_pag_ver_carrinho_IMP.gera(ses, cpr, erros)
