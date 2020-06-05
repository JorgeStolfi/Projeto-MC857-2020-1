
import html_lista_de_trechos_IMP

def gera(trcs, alterar):
  """Retorna um trecho de HTML que descreve os trechos em uma lista
  de trechos {trcs}.
  
  Cada trecho terá um botão "Ver" que, quando clicado, emitirá o comando 
  HTTP "ver_trecho" com o identificador do trecho como argumento.
  
  Se {alterar} for {True}, cada trecho também terá um botão "Alterar" que 
  emite o comando HTTP "solicitar_pag_alterar_trecho" com o 
  identificador do trecho como argumento."""
  return html_lista_de_trechos_IMP.gera(trcs, alterar)
