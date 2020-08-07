# Implementação do módulo {comando_encerrar_trecho}.

import html_pag_login
import html_pag_trecho
import usuario
import trecho
import poltrona
import sessao
import utils_testes
from valida_campo import ErroAtrib


def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, args):

  assert ses != None, "Este comando só pode ser usado após login"
  assert sessao.eh_administrador(ses), "Este comando é reservado para administradores"

  args = args.copy() # Por via das dúvidas.

  # Trecho a alterar:
  id_trc = args["id_trecho"] if 'id_trecho' in args else None
  assert id_trc != None # Paranoia (formulario deve incluir).
  args.pop("id_trecho")
  trc = trecho.busca_por_identificador(id_trc)
  assert trc != None
  
  try:
    atrs_muda = { 'encerrado': True }
    trecho.muda_atributos(trc, atrs_muda)

    # Repete a página de ver trecho com valores correntes (alterados):
    pag = html_pag_trecho.gera(ses, trc, None, "Trecho encerrado")

  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página de ver trecho com os mesmos argumentos e mens de erro:
    pag = html_pag_trecho.gera(ses, trc, args, erros)
  return pag
