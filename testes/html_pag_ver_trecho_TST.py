#! /usr/bin/env python3

import html_pag_ver_trecho
import tabelas
import usuario
import sessao
import trecho
import base_sql
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Sessao de teste de usuário comum:
ses_com = sessao.busca_por_identificador("S-00000001")
assert ses_com != None
assert not sessao.eh_administrador(ses_com)

# Usuario comum de teste:
usr_com = sessao.obtem_usuario(ses_com)
assert usr_com != None
usr_com_id = usuario.obtem_identificador(usr_com)
usr_com_atrs = usuario.obtem_atributos(usr_com)

# Sessao de teste de administrador:
ses_adm = sessao.busca_por_identificador("S-00000004")
assert ses_adm != None
assert sessao.eh_administrador(ses_adm)

# Usuario administrador de teste:
usr_adm = sessao.obtem_usuario(ses_adm)
assert usr_adm != None
usr_adm_id = usuario.obtem_identificador(usr_adm)
usr_adm_atrs = usuario.obtem_atributos(usr_adm)

# Trecho teste
trecho1 = trecho.busca_por_identificador("T-00000001")
assert trecho1 != None

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_pag_ver_trecho
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Testes com erros em vérios formatos:
for comprar_pols in (False, True):
  for alterar_trc in (False, True):
    ca = "-c" + str(comprar_pols) + "-a" + str(alterar_trc)
    for tag, erros in (
        ("N-E0", None), 
        ("N-E1", "Não entendi"), 
      ):
      ses = (ses_adm if alterar_trc else ses_com)
      testa(tag + ca, ses, trecho1, comprar_pols, alterar_trc, erros)
