# Implementação do módulo {comando_alterar_usuario}.

import html_pag_login
import html_pag_alterar_usuario
import usuario
import sessao
from utils_testes import erro_prog, mostra
from valida_campo import ErroAtrib
import re
import sys

def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, args):
  # Determina se o usuário corrente {usr_ses} é administrador:
  if ses == None:
    admin = False
  else:
    usr_ses = sessao.obtem_usuario(ses)
    assert usr_ses != None
    admin = usuario.obtem_atributos(usr_ses)['administrador']

  # Tenta editar o usuário:
  try:
    usuario.confere_e_elimina_conf_senha(args)
    usr = usuario.muda_atributos(args)
    pag = html_pag_login.gera(ses, None)   
  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página de cadastrar com os mesmos argumentos e mens de erro:
    pag = html_pag_alterar_usuario.gera(ses, args, erros)
  return pag
