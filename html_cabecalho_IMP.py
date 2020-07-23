import html_imagem_link


def gera(title, grande):

  if grande:
    ht_img = html_imagem_link.gera("13802.jpg", "logotipo", 60, "imagens/13802.jpg")
    header_title = "<h1>" + ht_img + " " + title + "</h1>"
  else:
    header_title = "<h2>" + title + "</h2>"

  return \
    "<!DOCTYPE HTML>\n" + \
    "<html>\n" + \
    "<head>\n" + \
    "<link rel=\"icon\" href=\"imagens/favicon.png\" type=\"image/x-icon\"> " +  \
    "<link rel=\"shortcut icon\" href=\"imagens/favicon.png\" type=\"image/x-icon\"> " +  \
    "<link rel=\"icon\" href=\"imagens/favicon-32x32.png\" sizes=\"32x32\"> " +  \
    "<link rel=\"shortcut icon\" href=\"imagens/favicon-32x32.png\" sizes=\"32x32\" type=\"image/png\"> " + \
    "<meta charset=\"UTF-8\"/>\n" + \
    "<title>" + title + "</title>\n" + \
    "</head>\n" + \
    "<body style=\"background-color:#eeeeee; text-indent: 0px\">\n" + \
    header_title
