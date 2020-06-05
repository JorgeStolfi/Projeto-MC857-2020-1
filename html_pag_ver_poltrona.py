import html_pag_ver_poltrona_IMP

def gera(ses, pol, excluir, erros):
  """Retorna uma página HTML que mostra os dados da poltrona {pol}
  (que deve ser um objeto de tipo {Objeto_Poltrona}).
  
  Se {excluir} for {True}, haverá um botão "Excluir" que emite o
  comando "excluir_poltrona_de_compra". """
  return html_pag_ver_poltrona_IMP.gera(ses, pol, excluir, erros)
