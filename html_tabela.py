import html_tabela_IMP

def tabela(linhas):
  """Gera o HTML para uma tabela "<table>...</table>".
  
  O parâmetro {linhas} deve ser uma lista ou tupla cujos elementos descrevem as linhas.
  Cada elemento de {linhas} deve ser uma list ou tupla de fragmentos HTML, que são 
  inseridos nas células da linha correspondente da tabela."""
  return html_tabela_IMP.gera(linhas)
