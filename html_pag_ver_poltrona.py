import html_pag_ver_poltrona_IMP

def gera(ses, pol, id_compra, excluir, erros):
  """Retorna uma página HTML que mostra os dados da poltrona {pol}
  (que deve ser um objeto de tipo {Objeto_Poltrona}).
  
  Se {excluir} for {True}, {id_compra} deve ser o identificador da compra atribuída a
  essa poltrona. No resultado, haverá um botão "Excluir" que emite o comando 
  "excluir_poltrona_de_compra".
  
  Se {excluir} for {False}, {id_compra deve ser {None} e não haverá um botão Excluir. """
  return html_pag_ver_poltrona_IMP.gera(ses, pol, id_compra, excluir, erros)
