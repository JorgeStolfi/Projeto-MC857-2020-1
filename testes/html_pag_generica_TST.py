#! /usr/bin/python3

import html_pag_generica
import tabelas
import usuario
import compra
import sessao
import base_sql
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()


def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_pag_generica
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = True  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


def fecha_sessoes(id_usr):
  sessoes = list(map(lambda id_ses: sessao.busca_por_identificador(id_ses), sessao.busca_por_usuario(id_usr)))
  for sessao_usr in sessoes:
    if sessao.aberta(sessao_usr):
      sessao.fecha(sessao_usr)


pag_conteudo = "Viagens Oito-Cinco-Sete"
id_usr_nao_admin = "U-00000001"
id_usr_admin = "U-00000003"

usr_nao_admin = usuario.busca_por_identificador(id_usr_nao_admin)
usr_admin = usuario.busca_por_identificador(id_usr_admin)

# Teste sem sessao
testa("sem_sessao", None, pag_conteudo, None)

# Fecha todas as sessoes
fecha_sessoes(id_usr_nao_admin)
fecha_sessoes(id_usr_admin)

# Teste com apenas uma sessao
# - Nao admin
ses = sessao.cria(usr_nao_admin, "ASDIHADBH", None)
testa("uma_sessao_nao_admin", ses, pag_conteudo, None)

# - Admin
ses = sessao.cria(usr_admin, "DASDASDD", None)
testa("uma_sessao_admin", ses, pag_conteudo, None)

# Teste com multiplas sessoes
# - Nao admin
ses = sessao.cria(usr_nao_admin, "GFHFGHHFG", None)
testa("varias_sessoes_nao_admin", ses, pag_conteudo, None)

# - Admin
ses = sessao.cria(usr_admin, "XCVJXCVVL", None)
testa("varias_sessoes_admin", ses, pag_conteudo, None)

# Teste de mensagens de erro
testa("lista_erro_vazia", ses, pag_conteudo, [])

testa("lista_error_populada", ses, pag_conteudo, ["Erro 1", "Erro 2", "Erro 3"])
