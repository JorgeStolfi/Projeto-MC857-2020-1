
def gera(nome, alt, tam):
  """Constrói o HTML para a imagem do produto {prod}, que aparecerá à 
  esquerda da descrição.  Os parâmetros são os mesmos de {bloco_de_produto}."""
  ht_img = ("<img src=\"imagens" + nome + "\" alt=\"" + alt + "\" style=\"float:left;height:%dpx;\"/>" % tam)
  return ht_img
  
