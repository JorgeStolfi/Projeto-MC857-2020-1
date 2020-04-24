import html_estilo_de_botao

def gera(texto, URL, args, cor_fundo):
  if args != None:
    # Acrescenta argumentos ao {URL}:
    sep = '?'
    for key, val in args.items():
      if val != None and val != "":
        URL += (sep + key + "=" + str(val))
        sep = '&'
    
  # Constrói o botão propriamente dito:
  estilo = html_estilo_de_botao.gera(cor_fundo)
  html = "<button type=\"button\" style=\"" + estilo + "\" onclick=\"location.href='" + URL + "'\">" + texto + "</button>"
  return html
