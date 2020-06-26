
def gera(nome, alt, tam):
  estilo = ("float:left;height:%dpx;" % tam);
  ht_img = ("<img src=\"imagens/" + nome + "\" alt=\"" + alt + "\" style=\"%s\"/>" % estilo)
  return ht_img
  
