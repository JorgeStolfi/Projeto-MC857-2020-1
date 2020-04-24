# Implementação do módulo {comando_fazer_logout}.

import html_pag_principal
import html_pag_mensagem_de_erro
import sessao
import processa_comando_http

def processa(ses, args):
  if ses == None or not sessao.aberta(ses):
    # Isto nunca deveria acontecer, mas em todo caso:
    pag = html_pag_mensagem_de_erro.gera(ses, "Precisa entrar no site antes de sair")
    ses_nova = ses
  else:
    sessao.fecha(ses)
    ses_nova = None
    pag = html_pag_principal.gera(ses_nova, None)
  return pag, ses_nova
