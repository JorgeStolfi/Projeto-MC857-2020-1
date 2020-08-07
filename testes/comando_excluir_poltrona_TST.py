#! /usr/bin/python3

import sys
import comando_excluir_poltrona
import base_sql
import tabelas

import sessao
import compra
import poltrona
import usuario
import trecho

from utils_testes import erro_prog, testa_gera_html

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando objetos...\n")
tabelas.cria_todos_os_testes(False)
def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = comando_excluir_poltrona
  funcao = modulo.processa
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Sessao de usuário comum e poltrona desse usuário:
ses_com1 = sessao.busca_por_identificador("S-00000003")
usr_com1 = sessao.obtem_usuario(ses_com1)
assert not usuario.obtem_atributo(usr_com1, 'administrador')
 
id_cpr_com1 = "C-00000003"
cpr_com1 = compra.busca_por_identificador(id_cpr_com1)
assert compra.obtem_cliente(cpr_com1) == usr_com1
id_pol_com1 = "A-00000008"
pol_com1 = poltrona.busca_por_identificador(id_pol_com1)
assert poltrona.obtem_atributo(pol_com1, "id_compra") == id_cpr_com1

testa("com1-com1", ses_com1, { 'id_poltrona': id_pol_com1 })


# Sessao de administrador e poltrona de outro usuário:
ses_adm3 = sessao.busca_por_identificador("S-00000004")
usr_adm3 = sessao.obtem_usuario(ses_adm3)
assert usuario.obtem_atributo(usr_adm3, 'administrador')

id_cpr_com2 = "C-00000001"
cpr_com2 = compra.busca_por_identificador(id_cpr_com2)
usr_com2 = compra.obtem_cliente(cpr_com2)
assert not usuario.obtem_atributo(usr_com2, 'administrador')
id_pol_com2 = "A-00000006"
pol_com2 = poltrona.busca_por_identificador(id_pol_com2)
assert poltrona.obtem_atributo(pol_com2, "id_compra") == id_cpr_com2

testa("adm3-com2", ses_adm3, { 'id_poltrona': id_pol_com2 })
