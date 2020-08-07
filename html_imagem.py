import html_imagem_IMP

def gera(nome, alt, tam):  
  """Constrói o HTML para a imagem "imagens/{nome}" com altura {tam} 
  e texto alternativo {alt}.  Se o arquivo não existir, exibe 
  "imagens/cinza.png"."""
  return html_imagem_IMP.gera(nome, alt, tam)
