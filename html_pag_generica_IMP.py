import sessao
import usuario
import compra

import html_cabecalho
import html_menu_geral
import html_rodape
import html_erro
import html_span

import re
import sys


def gera(ses, ht_conteudo, erros):
  # Cabeçalho das páginas:
  ht_cabe = html_cabecalho.gera("VIAGENS OITO-CINCO-SETE", True)

  logado = (ses != None)
  if logado:
    usr = sessao.obtem_usuario(ses)

    nome_usuario = usuario.obtem_atributos(usr)['nome']
    admin = usuario.obtem_atributos(usr)['administrador']
    id_usr = usuario.obtem_identificador(usr)
    num_ses = len(usuario.sessoes_abertas(usr));
    num_cpr = len(usuario.compras_abertas(usr));
    # sys.stderr.write("usuario %s num_ses = %d  num_cpr = %d\n" % (id_usr, num_ses, num_cpr))
#    assert not (admin and (num_cpr > 0)) # Administradores não devem ter compras.
  else:
    nome_usuario = None
    admin = False
    num_ses = 0
    num_cpr = 0

  # Menu geral no alto da página:
  ht_menu = html_menu_geral.gera(logado, nome_usuario, admin)

  # Mensagem de multiplas sessoes:
  if num_ses > 1:
    estilo_multi_ses = None; # cor_texto = "#FF0000" cor_fundo = "#eeeeee"
    if num_ses == 2:
      ht_multi_ses = html_span.gera(estilo_multi_ses, "Você tem outra sessao aberta.")
    else:
      ht_multi_ses = html_span.gera(estilo_multi_ses, "Você tem outras %d sessoes abertas." % (num_ses-1))
  else:
    ht_multi_ses = None

  # Mensagem de multiplas compras:
  if num_cpr > 1:
    estilo_multi_cpr = None; # cor_texto = "#FF0000" cor_fundo = "#eeeeee"
    if num_cpr == 2:
      ht_multi_cpr = html_span.gera(estilo_multi_cpr, "Você tem outra compra aberta.")
    else:
      ht_multi_cpr = html_span.gera(estilo_multi_cpr, "Você tem outras %d compras abertas." % (num_cpr-1))
  else:
    ht_multi_cpr = None

  # Mensagens de erro - quebra e limpa:
  if erros == None:
    erros = []
  elif type(erros) == str:
    # Split lines, create a list:
    erros = re.split('[\n]', erros)
  assert type(erros) is list or type(erros) is tuple
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
    ( ht_multi_ses + "<br/>\n" if ht_multi_ses != None else "" ) + \
    ( ht_multi_cpr + "<br/>\n" if ht_multi_cpr != None else "" ) + \
    ht_erros + "<br/>\n" + \
    ht_conteudo + "<br/>\n" + \
    ht_roda
  return pagina
