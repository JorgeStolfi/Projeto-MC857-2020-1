# Implementação do módulo {comando_fechar_sessao}.

import html_pag_sessao
import html_pag_mensagem_de_erro
import html_pag_principal
import sessao

def processa(ses, args):
  assert ses != None and sessao.aberta(ses) # Paranóia.
  
  # Obtem a sessão a fechar (pode ser diferente de {ses}:
  id_ses_fech = args['id_sessao'] if 'id_sessao' in args else None
  assert id_ses_fech != None # Paranóia (formulário deveria especificar)
  ses_fech = sessao.busca_por_identificador(id_ses_fech)
  assert ses_fech != None # Paranóia.
  
  try:
    sessao.fecha(ses_fech)
    erros = []
  except ErroAtrib as ex:
    erros = ex[0]

  if ses == ses_fech and not sessao.aberta(ses):
    # A sessao que foi fechada é a sessao corrente.
    # Fazer como em comando_fazer_logout:
    pag = html_pag_principal.gera(None, erros)
    ses_nova = None
  else:
    # A sessão corrente não foi fechada.
    # Mostra a página da sessão que deveria ser fechada, com erros se houve:
    pag = html_pag_sessao.gera(ses, ses_fech, erros)
    ses_nova = ses

  return pag, ses_nova
