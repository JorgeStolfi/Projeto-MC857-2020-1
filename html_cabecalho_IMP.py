def gera(title, grande):

  if grande:
    header_title = "<h1>" + title + "</h1>"
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
