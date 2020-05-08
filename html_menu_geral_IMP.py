import html_botao_simples
import html_bloco_texto
from utils_testes import erro_prog

# Outros módulos importados por esta implementação:
from datetime import datetime, timezone
import re
import sys

def gera(logado, nome_usuario, admin):
  html_menu = gera_linha(gera_botoes_linha_1(logado, nome_usuario, admin))
  if admin:
    html_menu += gera_linha(gera_botoes_linha_2())
  return html_menu

def gera_linha(botoes):
  """Monta uma linha do menu geral, dada uma lista de fragmentos HTML que
  descrevem os botões."""
  html = "<nav>"
  for bt in botoes:
    if bt != None and bt != "":
      html += "  " + bt
  html += "</nav>"
  return html

def gera_botoes_linha_1(logado, nome_usuario, admin):
  """Gera uma lista de fragmentos de HTML que descrevem os botões da linha 1 do menu
  geral.  Estes botões são mostrados para todos os usuários, mas
  dependem do tipo de usuário (normal ou administrador) e se o
  usuário está logado."""

  # Botões da primeira linha que sempre aparecem:
  html_bt_principal = html_botao_simples.gera("Principal", 'principal', None, '#60a3bc')
  # html_bt_ofertas = html_botao_simples.gera("Ofertas", 'ver_ofertas', None, '#ffdd22')
  html_bt_ofertas = None
  # html_fm_buscar = html_form_buscar_site.gera()
  html_fm_buscar = None
  botoes = ( html_bt_principal, html_bt_ofertas, html_fm_buscar)
  if logado:
    # Gera outros botões de usuario normal logado
    botoes += gera_botoes_linha_1_logado(nome_usuario, admin)
  else:
    # Gera outros botões de usuário deslogado:
    botoes += gera_botoes_linha_1_deslogado()
  return botoes

def gera_botoes_linha_1_logado(nome_usuario, admin):
  """Gera uma lista de fragmentos HTML com os botões da linha 1 do menu
  geral, para um usuário que está logado."""
  botoes_sempre = (
      html_botao_simples.gera("Minha Conta", 'solicitar_pag_alterar_usuario', None, '#eeeeee'),
      html_botao_simples.gera("Contato", 'solicitar_pag_contato', None, '#eeeeee'),
      html_botao_simples.gera("Sair", 'fazer_logout', None, '#eeeeee'),
      gera_nome_usuario(nome_usuario)
    )
  if admin:
    botoes_compras = ( )
  else:
    botoes_compras = (
      html_botao_simples.gera("Meu Carrinho", 'ver_carrinho', None, '#eeeeee'),
      html_botao_simples.gera("Minhas Compras", 'buscar_compras', None, '#eeeeee'),
    )
  return botoes_sempre + botoes_compras

def gera_botoes_linha_1_deslogado():
  """Gera uma lista de fragmentos HTML com os botões da linha 1 do menu
  geral, para um usuário que não está logado."""
  botoes = (
    html_botao_simples.gera("Entrar", 'solicitar_pag_login', None, '#55ee55'),
    html_botao_simples.gera("Cadastrar", 'solicitar_pag_cadastrar_usuario', None, '#eeeeee'),
  )
  return botoes

def gera_botoes_linha_2():
  """Gera uma lista de fragmentos de HTML com os botões da linha 2 do menu
  geral.  Estes botãoes são mostrados apenas se o usuário está logado
  e é um administrador."""

  botoes = (
    html_botao_simples.gera("Acrescentar trecho", "solicitar_pag_acrescentar_trecho", None, '#ffdd22'),
    # html_botao_simples.gera("Alterar trecho", "solicitar_pag_alterar_trecho", None, '#ffdd22'),
    # html_form_passageiros.gera(),
    # html_form_buscar_objeto.gera(),
  )
  return botoes

def gera_nome_usuario(nome_usuario):
  """Gera o texto "Oi {nome}" para o menu geral."""
  res = html_bloco_texto.gera("Oi " + nome_usuario, "inline_block", "Courier", "18px", "bold", None, None, None, None),
