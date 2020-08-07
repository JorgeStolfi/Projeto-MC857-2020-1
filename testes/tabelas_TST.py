#! /usr/bin/python3
# Teste do módulo {tabelas}

import base_sql
import tabelas
import usuario
import compra
import sessao
import poltrona
import trecho
import sys

# ----------------------------------------------------------------------

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res == None

# ----------------------------------------------------------------------

sys.stderr.write("Abrindo as tabelas...\n")
tabelas.inicializa_todas(False)
tabelas.cria_todos_os_testes(False)

# ----------------------------------------------------------------------
sys.stderr.write("verificando tabela \"usuarios\" usr = %s\n" % "usr1") 

usr1_id = "U-00000001"
usr1 = usuario.busca_por_identificador(usr1_id)
assert usr1 != None
usr1_atrs = usuario.obtem_atributos(usr1)
usuario.verifica(usr1, usr1_id, usr1_atrs)

assert usr1 == tabelas.id_para_objeto(usr1_id)

sys.stderr.write("\n")

# ----------------------------------------------------------------------
sys.stderr.write("verificando tabela \"sessao\", ses = %s\n" % "ses1") 

ses1_id = "S-00000001"
ses1 = sessao.busca_por_identificador(ses1_id)
assert ses1 != None
ses1_atrs = sessao.obtem_atributos(ses1)
sessao.verifica(ses1, ses1_id, ses1_atrs)

assert ses1 == tabelas.id_para_objeto(ses1_id)

sys.stderr.write("\n")

# ----------------------------------------------------------------------
sys.stderr.write("verificando tabela \"compras\" cpr = %s\n" % "cpr1") 

cpr1_id = "C-00000001"
cpr1 = compra.busca_por_identificador(cpr1_id)
assert cpr1 != None
cpr1_atrs = compra.obtem_atributos(cpr1)
compra.verifica(cpr1, cpr1_id, cpr1_atrs)

assert cpr1 == tabelas.id_para_objeto(cpr1_id)

sys.stderr.write("\n")

# ----------------------------------------------------------------------
sys.stderr.write("verificando tabela \"poltronas\" ptr = %s\n" % "ptr1")

ptr1_id = "A-00000001"
ptr1 = poltrona.busca_por_identificador(ptr1_id)
assert ptr1 != None
ptr1_atrs = poltrona.obtem_atributos(ptr1)
poltrona.verifica(ptr1, ptr1_id, ptr1_atrs)

assert ptr1 == tabelas.id_para_objeto(ptr1_id)

sys.stderr.write("\n")

# ----------------------------------------------------------------------
sys.stderr.write("verificando tabela \"trechos\" trc = %s\n" % "trc1")

trc1_id = "T-00000001"
trc1 = trecho.busca_por_identificador(trc1_id)
assert trc1 != None
trc1_atrs = trecho.obtem_atributos(trc1)
trecho.verifica(trc1, trc1_id, trc1_atrs)

assert trc1 == tabelas.id_para_objeto(trc1_id)

sys.stderr.write("\nTestes terminaram sem erros.\n\n")
