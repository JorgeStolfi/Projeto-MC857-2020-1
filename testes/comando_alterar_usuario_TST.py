#! /usr/bin/python3

import comando_alterar_usuario
import tabelas
import usuario
import sessao
import base_sql
import utils_testes

import sys

# Conecta no banco e carrega alimenta com as informações para o teste


sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = comando_alterar_usuario
    funcao = modulo.processa
    frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

def testa_atualiza_atributo(rot, ses, args):
  assert 'id_usuario' in args
  testa(rot, ses, args)
  id_usr = args['id_usuario']
  usr = usuario.busca_por_identificador(id_usr)
  atrs_usr = usuario.obtem_atributos(usr)
  for ch, val in atrs_usr.items():
    if ch in args:
      assert val == args[ch], ("campo '%s' = '%s' não foi alterado para '%s'\n" % (ch, val, args[ch]))

# ----------------------------------------------------------------------
# Usuário comum alterando seus próprios dados:
ses_com1 = sessao.busca_por_identificador("S-00000001")
usr_com1 = sessao.obtem_usuario(ses_com1)
assert not usuario.obtem_atributo(usr_com1, 'administrador')
id_usr_com1 = usuario.obtem_identificador(usr_com1);

args_alt1_com1 = args = { 
   'id_usuario': id_usr_com1, 
   'nome': "John First", 
   'telefone': "007", 
   'senha': "111",
   'conf_senha': "111",
 }

testa_atualiza_atributo("sesC-usrC", ses_com1, args_alt1_com1)
   
# ----------------------------------------------------------------------
# Administrador alterando usuário comum e promovendo a administrador:
ses_adm3 = sessao.busca_por_identificador("S-00000004")
usr_adm3 = sessao.obtem_usuario(ses_adm3)
assert usuario.obtem_atributo(usr_adm3, 'administrador')
id_usr_adm3 = usuario.obtem_identificador(usr_adm3);

args_alt2_com1 = args = { 
  'id_usuario': id_usr_com1, 
  'nome': "Giovanni Primo", 
  'telefone': "(011)2-2322",
  'administrador': True,
 }

testa_atualiza_atributo("sesA-usrC", ses_adm3, args_alt2_com1)

# ----------------------------------------------------------------------
# Administrador alterando outro administrador e rebaixando:
usr_adm8 = usuario.busca_por_identificador("U-00000008")
assert usuario.obtem_atributo(usr_adm8, 'administrador')
id_usr_adm8 = usuario.obtem_identificador(usr_adm8);

args_alt3_adm8 = args = { 
  'id_usuario': id_usr_adm8, 
  'nome': "François Huitième", 
  'telefone': "+99(99)9-999",
  'administrador': False,
 }

testa_atualiza_atributo("sesA-usrA", ses_adm3, args_alt3_adm8)
