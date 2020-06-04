import html_pag_ver_roteiro_IMP

def gera(ses, rot):
  """Retorna uma página HTML que mostra os dados do roteiro {rot}
  (que deve ser uma lista de objetos do tipo {Objeto_Trecho}).
  
  A página terá um cabeçalho com resumo das informações do roteiro
  (vide {html_resumo_de_roteiro.gera}) e em seguida uma lista dos trechos
  do roteiro.
  
  Cada linha terá um botão "Ver", que, quando clicado, 
  emitirá o comando HTTP "ver_trecho" com o identificador do 
  trecho como argumento."""
  return html_pag_ver_roteiro_IMP.gera(ses, rot)
