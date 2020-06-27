import html_resumo_de_poltrona_de_usuario_IMP

def gera(pol):
  """Devolve um fragmento HTML que decreve a poltrona {pol}, 
  um objeto da classe {Objeto_Poltrona}.  A poltrona deve ser
  associada à um usuário.
  
  O fragmento mostra os dados essenciais do trecho ao qual a poltrona
  pertence (identificador "T-{NNNNNNNN}", código do voo, porto, dia, e hora de 
  partida e chegada), o número da poltrona, e o preço.
  
  Em qualquer caso, será monstrado um botão "Ver", que, quando clicado,
  emite of comando HTTP "ver_poltrona", com 
  argumento {'id_poltrona': id_poltrona}.
   
  O resultado não é um string, mas uma tupla com um string separado 
  para cada campo ou botão.  Esta tupla deve ser usada como uma linha do
  argumento de {html_table}."""
  return html_resumo_de_poltrona_de_usuario_IMP.gera(pol)
