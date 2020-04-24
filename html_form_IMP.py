def form(estilo, conteudo):
  est = (" style=\"" + estilo + "\"" if estilo != None and estilo != "" else "")
  html = "<form method=\"post\"" + est + ">" + conteudo + "</form>"
  return html
