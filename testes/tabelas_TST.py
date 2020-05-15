#! /usr/bin/python3
# Teste do módulo {tabelas}

import base_sql
import tabelas
import usuario
import compra
import sys

# ----------------------------------------------------------------------

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res == None

# ----------------------------------------------------------------------

sys.stderr.write("Abrindo as tabelas...\n")
tabelas.inicializa_todas(False)
tabelas.cria_todos_os_testes()

# ----------------------------------------------------------------------
sys.stderr.write("verificando tabela \"usuarios\" usr = %s\n" % "usr1") 

usr1_id = "U-00000001"
usr1 = usuario.busca_por_identificador(usr1_id)
assert usr1 != None
usr1_atrs = usuario.obtem_atributos(usr1)
usuario.verifica(usr1, usr1_id, usr1_atrs)

assert usr1 == tabelas.id_para_opbjeto(usr1_id)

sys.stderr.write("\n")

# ----------------------------------------------------------------------
sys.stderr.write("verificando tabela \"sessao\", ses = %s\n" % "ses1") 

ses1_id = "S-00000001"
ses1 = sessao.busca_por_identificador(ses1_id)
assert ses1 != None
ses1_atrs = sessao.obtem_atributos(ses1)
sessao.verifica(ses1, ses1_id, ses1_atrs)

assert ses1 == tabelas.id_para_opbjeto(ses1_id)

sys.stderr.write("\n")

# ----------------------------------------------------------------------
sys.stderr.write("verificando tabela \"compras\" cpr = %s\n" % "cpr1") 

cpr1_id = "C-00000001"
cpr1 = compra.busca_por_identificador(cpr1_id)
assert cpr1 != None
cpr1_atrs = compra.obtem_atributos(cpr1)
compra.verifica(cpr1, cpr1_id, cpr1_atrs)

assert cpr1 == tabelas.id_para_opbjeto(cpr1_id)

sys.stderr.write("\n")

# ----------------------------------------------------------------------
assert False # !!! INCOMPLETO - TESTAR TABELAS "assentos", "trechos"
