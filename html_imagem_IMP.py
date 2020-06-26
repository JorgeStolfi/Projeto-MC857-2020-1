
def gera(nome, alt, tam):
  """Constrói o HTML para a imagem solicitada (produto, logotipo). Para produto,
  a imagem que aparecerá à esquerda da descrição.  Os parâmetros são os mesmos
  de {bloco_de_produto}."""

  #Se receber valor {None}, converte string para vazia
  if nome is None:
      nome = ""

  #Se campo nome não for string {vazia} carrega imagem solicitada, senão carrega imagem cinza.png
  if nome and not nome.isspace():
      ht_img = ("<img src=\"imagens/" + nome + "\" alt=\"" + alt + "\" style=\"float:left;height:%dpx;\"/>" % tam)
  else:
      ht_img = ("<img src=\"imagens/cinza.png" + nome + "\" alt=\"" + alt + "\" style=\"float:left;height:%dpx;\"/>" % tam)

  return ht_img
