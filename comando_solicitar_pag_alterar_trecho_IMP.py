import html_pag_trecho
import html_pag_mensagem_de_erro
import sessao
import usuario
import trecho
from valida_campo import ErroAtrib

def processa(ses, args):
  
  admin = False if ses == None else sessao.eh_administrador(ses)
  assert admin # Paranóia (cliente comum e deslogado não deveria ter acesso a este cmd).

  # Obtem o trecho a alterar:
  id_trc = args['id_trecho'] if 'id_trecho' in args else None
  assert id_trc != None # Paranóia (formulário deveria especificar).
  trc = trecho.busca_por_identificador(id_trc)
  assert trc != None # Paranóia.
  
  pag = html_pag_trecho.gera(ses, trc, None, None)
  return pag
    
