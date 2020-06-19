
import html_lista_de_trechos_IMP

def gera(trcs, alterar):
  """Retorna um trecho de HTML que descreve da lista
  de trechos {trcs} (objetos do tipo {Objeto_Trecho}).
  
  Cada trecho terá um botão "Ver" que, quando clicado, emitirá o comando 
  HTTP "ver_trecho" com argumentos { 'id_trecho': id_trecho }.
  
  Se {alterar} for {True}, cada trecho também terá um botão "Alterar" que 
  emite o comando HTTP "solicitar_pag_alterar_trecho" com o 
  identificador do trecho como argumento.  (Estes botões deveriam ser
  solicitados apenas quando o dono da sessão é um administrador.) """
  return html_lista_de_trechos_IMP.gera(trcs, alterar)
