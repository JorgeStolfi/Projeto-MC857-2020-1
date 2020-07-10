# Implementação do módulo {comando_alterar_trecho}.

import html_pag_login
import html_pag_alterar_trecho
import usuario
import trecho
import sessao
import utils_testes
from valida_campo import ErroAtrib


def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, args):

  args = args.copy() # Por via das dúvidas.

  # Determina se o usuário corrente {usr_ses} é administrador:
  if ses == None:
    # Não deveria acontecer:
    utils_testes.erro_prog("usuário deveria estar logado")
  else:
    usr_ses = sessao.obtem_usuario(ses)
    assert usr_ses is not None
    admin = usuario.obtem_atributos(usr_ses)['administrador']

  id_trc = args["id_trecho"]
  assert id_trc is not None, "id_trecho obrigatório para atualizar"
  args.pop("id_trecho")

  # Tenta editar o trecho:
  try:
    trc = trecho.busca_por_identificador(id_trc)
    trecho.muda_atributos(trc, args)
    
    # Repete a página de alterar trecho com valores correntes (alterados):
    args_novo = trecho.obtem_atributos(trc)
    pag = html_pag_alterar_trecho.gera(ses, id_trc, args_novo, None)
  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página de alterar trecho com os mesmos argumentos e mens de erro:
    pag = html_pag_alterar_trecho.gera(ses, id_trc, args, erros, False)
  return pag
