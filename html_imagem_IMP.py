import os.path
import re

def gera(nome, alt, tam):
  """Constrói o HTML para a imagem solicitada (produto, logotipo). Para produto,
  a imagem que aparecerá à esquerda da descrição.  Os parâmetros são os mesmos
  de {bloco_de_produto}."""
  
  # Consistência no nome do arquivo:
  assert nome == None or re.fullmatch(r'[-_A-Za-z0-9./]+', nome);

  # Se imagem não existir ou nome for {None}, usa "cinza.png"
  if nome == None:
    arq = "imagens/cinza.png"
  else:
    arq = "imagens/" + nome
    if not os.path.isfile(arq): arq = "imagens/cinza.png"
  
  ht_estilo = ( " style=\"float:left;height:%dpx;\"" % tam )
  ht_img = ("<img src=\"" + arq + "\" alt=\"" + alt + "\"" + ht_estilo + "/>")

  return ht_img
