# Implementação do módulo {comando_alterar_usuario}.

import html_pag_login
import html_pag_usuario
import usuario
import sessao
from valida_campo import ErroAtrib


def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo


def processa(ses, args):

  # Determina se o usuário corrente {usr_ses} é administrador:
  if ses is None:
    usr_ses = None
    admin = False
  else:
    usr_ses = sessao.obtem_usuario(ses)
    assert usr_ses is not None
    admin = usuario.obtem_atributos(usr_ses)['administrador']

  id_usr = args["id_usuario"] if "id_usuario" in args else None
  assert id_usr is not None, "id_usuario obrigatório para atualizar"

  usr = usuario.busca_por_identificador(id_usr)

  # Tenta editar o usuário:
  try:
    if usr == None: raise ErroAtrib("esse usuário não existe")

    atrs_muda = args.copy()
    del atrs_muda["id_usuario"]
    usuario.confere_e_elimina_conf_senha(atrs_muda)

    usuario.muda_atributos(usr, atrs_muda)
    
    # Mostra de novo a página de alterar com dados novos:
    args_novos = usuario.obtem_atributos(usr)
    pag = html_pag_usuario.gera(ses, usr, args_novos, None)
  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página de cadastrar com os mesmos argumentos e mens de erro:
    pag = html_pag_usuario.gera(ses, usr, args, erros)
  return pag
