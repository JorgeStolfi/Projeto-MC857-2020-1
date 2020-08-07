import html_pag_trecho
import html_pag_generica
import sys
from valida_campo import ErroAtrib
import sessao

def processa(ses, args):
  admin = False if ses == None else sessao.eh_administrador(ses)
  assert admin  # Paranóia (cliente comum e deslogado não deveria ter acesso).

  assert not 'id_trecho' in args # Paranóia  (formulário não deveria ter este campo).
  pag = html_pag_trecho.gera(ses, None, None, None)
  return pag
