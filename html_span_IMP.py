def gera(estilo, conteudo):
  est = (" style=\"" + estilo + "\"" if estilo != None and estilo != "" else "")
  html = "<span" + est + ">" + conteudo + "</span>"
  return html
