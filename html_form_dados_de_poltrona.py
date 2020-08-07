import html_form_dados_de_poltrona_IMP

def gera(id_pol, atrs, admin, ht_submit):
  """Devolve um fragmento HTML "<form>...</form>" que decreve a poltrona
  {pol} cujo identificador é {id_pol} (que não pode ser {None})..

  O formulário vai conter um elemento <table>..</table> onde cada linha
  mostra um dos atributos de um {Objeto_Poltrona}. Os valores desses
  campos são inicializados conforme o dicionário {atrs} (e NÃO com os
  atributos correntes da poltrona).
  
  O parãmetro {admin} diz se o usuário que pediu estes dados é 
  administrador.  Se for {True}, o identificador da poltrona será visível, e alguns campos serão
  editáveis, incluindo o preço e o indicador de "oferta".
  """
  return html_form_dados_de_poltrona_IMP.gera(id_pol, atrs, admin, ht_submit)
