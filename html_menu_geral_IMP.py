import html_botao_simples
import html_texto
from utils_testes import erro_prog

# Outros módulos importados por esta implementação:
from datetime import datetime, timezone
import re
import sys

def gera(logado, nome_usuario, admin):
  ht_menu = gera_linha(gera_botoes_linha_1(logado, nome_usuario, admin))
  if admin:
    ht_menu += gera_linha(gera_botoes_linha_2())
  return ht_menu

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
  ht_bt_principal = html_botao_simples.gera("Principal", 'principal', None, '#60a3bc')
  ht_bt_ofertas = html_botao_simples.gera("Ofertas", 'solicitar_pag_ofertas', None, '#ffdd22')
  ht_bt_trechos = html_botao_simples.gera("Buscar Trechos", 'solicitar_pag_buscar_trechos', None, '#eeeeee')
  ht_bt_roteiros = html_botao_simples.gera("Buscar Roteiros", 'solicitar_pag_criar_roteiro', None, '#eeeeee')
  
  botoes = ( ht_bt_principal, ht_bt_ofertas, ht_bt_trechos, ht_bt_roteiros )
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
    html_botao_simples.gera("Buscar usuários", 'buscar_usuarios', None, '#eeeeee'),
    html_botao_simples.gera("Buscar compras", 'buscar_compras', None, '#eeeeee'),
    botoes_compras = ( )
  else:
    botoes_compras = (
      html_botao_simples.gera("Meu Carrinho", 'ver_carrinho', None, '#eeeeee'),
      html_botao_simples.gera("Minhas Compras", 'ver_minhas_compras', None, '#eeeeee'),
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
  geral.  Estes botões são mostrados apenas se o usuário está logado
  e é um administrador."""

  botoes = (
    html_botao_simples.gera("Acrescentar trecho", "solicitar_pag_acrescentar_trecho", None, '#ffdd22'),
    html_botao_simples.gera("Checar Objeto", 'ver_objeto', None, '#ffdd22'),
    # html_botao_simples.gera("Alterar trecho", "solicitar_pag_alterar_trecho", None, '#ffdd22'),
    # html_form_passageiros.gera(),
    # html_form_buscar_objeto.gera(),
  )
  return botoes

def gera_nome_usuario(nome_usuario):
  """Gera o texto "Oi {nome}" para o menu geral."""
  res = html_texto.gera("Oi " + nome_usuario, "inline_block", "Courier", "18px", "bold", None, None, None, None),
