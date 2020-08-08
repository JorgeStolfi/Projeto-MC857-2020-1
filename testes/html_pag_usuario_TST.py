#! /usr/bin/python3

from utils_testes import erro_prog, aviso_prog
import html_pag_usuario
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
tabelas.cria_todos_os_testes(False)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Função de teste de gerador de HTML

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_pag_usuario
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Dados para teste

# Sessao de teste de usuário administrador:
ses_adm3 = sessao.busca_por_identificador("S-00000004")
assert ses_adm3 != None
assert sessao.eh_administrador(ses_adm3)
usr_adm3 = sessao.obtem_usuario(ses_adm3)

# Sessao de teste cujo usuario não é admin:
ses_com1 = sessao.busca_por_identificador("S-00000001")
assert ses_com1 != None
assert not sessao.eh_administrador(ses_com1)
usr_com1 = sessao.obtem_usuario(ses_com1)

# Usuario teste comum:
usr_com2 = usuario.busca_por_identificador("U-00000002")
assert usr_com2 != None
assert not usuario.obtem_atributo(usr_com2, 'administrador')
usr_com2_id = usuario.obtem_identificador(usr_com2)
usr_com2_atrs = usuario.obtem_atributos(usr_com2)

# Usuario de teste que é administrador (nao o mesmo):
usr_adm8 = usuario.busca_por_identificador("U-00000008")
assert usr_adm8 != None
usr_adm8_id = usuario.obtem_identificador(usr_adm8)
usr_adm8_atrs = usuario.obtem_atributos(usr_adm8)

# Atributos de novo usuário:
usr_new1_atrs = {
  'nome': "Zebedeu Zaaratustra", 
  'senha': "99999999", 
  'email': "zaratustra@gmail.com", 
  'CPF': "999.888.777-00", 
  'telefone': "+55(19)9 9876-5432",
  'documento': "9.999.999-9 SSP-SP",
  'milhagem': 999,
  'administrador': False
}

# Atributos para alteração de usuário:
usr_alt1_atrs = {
  'nome': "José Alterado Primeiro", 
  'senha': "111111111", 
  'email': "primeiro@gmail.com", 
  'CPF': "123.456.789-00", 
  'milhagem': None,
  'administrador': False
}

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Testes com erros em vários formatos:
for etag, erros in (
    ("errN", None),
    ("errV", []),
    ("errL", ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",])
  ):
  for utag, ses, usr, atrs in (
      ("logN-usrN-atrC", None,     None,     usr_new1_atrs, ), # Criaçao de usuário sem login.
      ("logC-usrN-atrC", ses_com1, None,     usr_new1_atrs, ), # Criaçao de usuário por cliente.
      ("logA-usrN-atrC", ses_adm3, None,     usr_new1_atrs, ), # Criaçao de usuário por admin.
      ("logA-usr1-atrN", ses_adm3, usr_com1, None,          ), # isualização de usuário por admin.
      ("logA-usr1-atrA", ses_adm3, usr_com1, usr_alt1_atrs, ), # Alteração de usuário por admin.
      ("logC-usr1-atrA", ses_com1, usr_com1, usr_alt1_atrs, ), # Alteração de cliente por ele mesmo.
    ):
    rotulo = utag + "-" + etag
    testa(rotulo, ses, usr, atrs, erros)
