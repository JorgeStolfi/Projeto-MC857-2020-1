# Implementação do módulo {comando_encerrar_trecho}.

import html_pag_login
import html_pag_ver_trecho
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
  assert 'id_trecho' in args, "Faltou o parâmetro 'id_trecho'"
  id_trc = args["id_trecho"]
  args.pop("id_trecho")
  try:
    trc = trecho.busca_por_identificador(id_trc)
    atrs_muda = { 'aberto': False }
    trecho.muda_atributos(trc, atrs_muda)

    # Repete a página de ver trecho com valores correntes (alterados):
    comprar_pols = False  # Pois o dono da sessão deve ser admin, que não pode comprar.
    alterar_trc = True    # Pois o dono da sessão deve ser admin.
    pag = html_pag_ver_trecho.gera(ses, trc, comprar_pols, alterar_trc, None)

  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página de ver trecho com os mesmos argumentos e mens de erro:
    comprar_pols = False  # Pois o dono da sessão deve ser admin, que não pode comprar.
    alterar_trc = True    # Pois o dono da sessão deve ser admin.
    pag = html_pag_ver_trecho.gera(ses, trc, compar_pols, alterar_trc, erros)

  return pag
