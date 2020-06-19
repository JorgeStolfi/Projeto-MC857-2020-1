import html_imagem_link_IMP 

def gera(nome, alt, tam, url):
  """Constrói o HTML para a imagem "imagens/{nome}" com altura {tam} 
  e texto alternativo {alt}.  Quando o usuário clica na imagem, é emitido
  um comando HTTP GET com o {url} dado."""
  return html_imagem_link_IMP.gera(nome, alt, tam, url)
