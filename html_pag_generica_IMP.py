import sessao
import usuario

import html_cabecalho
import html_menu_geral
import html_rodape
import html_bloco_de_erro

import re

def gera(ses, html_conteudo, erros):

  # Cabeçalho das páginas:
  html_cabe = html_cabecalho.gera("Site de compras: Projeto MC857A 2020-1", True)

  # Menu geral no alto da página:
  logado = (ses != None)
  if logado:
    usr = sessao.obtem_usuario(ses)
    nome_usuario = usuario.obtem_atributos(usr)['nome']
    admin = usuario.obtem_atributos(usr)['administrador']
  else:
    nome_usuario = None
    admin = False
  html_menu = html_menu_geral.gera(logado, nome_usuario, admin)

  # Mensagens de erro:
  if erros == None:
    erros = []
  elif type(erros) == str:
    # Split lines, create a list:
    erros = re.split('[\n]', erros)
  assert type(erros) is list
  # Cleanup the messages:
  erros = [ er.strip() for er in erros ]
  erros = [ er for er in erros if len(er) > 0 ]
  if len(erros) != 0:
    erros = "<br/>\n" + "<br/>\n".join(erros)
    html_erros = html_bloco_de_erro.gera(erros) + "\n"
  else:
    html_erros = ""

  # Rodapé da página:
  html_roda = html_rodape.gera()

  # Monta a página:
  pagina = \
    html_cabe + "<br/>\n" + \
    html_menu + "<br/>\n" + \
    html_erros + "<br/>\n" + \
    html_conteudo + "<br/>\n" + \
    html_roda
  return pagina

