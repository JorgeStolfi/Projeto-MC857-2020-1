# Implementação do módulo {comando_alterar_trecho}.

import html_pag_login
import html_pag_trecho
import usuario
import trecho
import sessao
import utils_testes
from valida_campo import ErroAtrib


def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, args):

  args = args.copy() # Por via das dúvidas.

  id_trc = args["id_trecho"]
  assert id_trc !=  None # Paranóia (formulário deve incluir).
  args.pop("id_trecho")
  trc = trecho.busca_por_identificador(id_trc)
  assert trc != None # Paranóia.

  # Tenta editar o trecho:
  try:
    trecho.muda_atributos(trc, args)
    # Repete a página de alterar trecho com valores correntes (alterados):
    pag = html_pag_trecho.gera(ses, trc, None, None)
  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página de alterar trecho com os mesmos argumentos e mens de erro:
    pag = html_pag_trecho.gera(ses, trc, args, erros)
  return pag
