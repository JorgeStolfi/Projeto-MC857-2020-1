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
    "<meta charset=\"UTF-8\"/>\n" + \
    "<title>" + title + "</title>\n" + \
    "</head>\n" + \
    "<body style=\"background-color:#eeeeee; text-indent: 0px\">\n" + \
    header_title
