import sessao
import usuario

import html_cabecalho
import html_menu_geral
import html_rodape
import html_erro

import re

def gera(ses, ht_conteudo, erros):

  # Cabeçalho das páginas:
  ht_cabe = html_cabecalho.gera("VIAGENS OITO-CINCO-SETE", True)

  # Menu geral no alto da página:
  logado = (ses != None)
  if logado:
    usr = sessao.obtem_usuario(ses)
    nome_usuario = usuario.obtem_atributos(usr)['nome']
    admin = usuario.obtem_atributos(usr)['administrador']
  else:
    nome_usuario = None
    admin = False
  ht_menu = html_menu_geral.gera(logado, nome_usuario, admin)

  # Mensagens de erro:
  if erros == None:
    erros = []
  elif type(erros) == str:
    # Split lines, create a list:
    erros = re.split('[\n]', erros)
  assert type(erros) is list
  # Cleanup the messages:
  erros = [ er for er in erros if er != None ]
  erros = [ er.strip() for er in erros ]
  erros = [ er for er in erros if len(er) > 0 ]
  if len(erros) != 0:
    erros = "<br/>\n" + "<br/>\n".join(erros)
    ht_erros = html_erro.gera(erros) + "\n"
  else:
    ht_erros = ""

  # Rodapé da página:
  ht_roda = html_rodape.gera()

  # Monta a página:
  pagina = \
    ht_cabe + "<br/>\n" + \
    ht_menu + "<br/>\n" + \
    ht_erros + "<br/>\n" + \
    ht_conteudo + "<br/>\n" + \
    ht_roda
  return pagina

