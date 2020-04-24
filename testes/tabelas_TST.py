#! /usr/bin/python3
# Teste do módulo {tabelas}

import base_sql
import tabelas
import sys
from bs4 import BeautifulSoup as bsoup  # Pretty-print of HTML

# ----------------------------------------------------------------------

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res == None

# ----------------------------------------------------------------------

sys.stderr.write("Abrindo as tabelas...\n")
tabelas.inicializa_todas(False)

# ----------------------------------------------------------------------
sys.stderr.write("testando {utils_testes.verifica_objeto}\n") 

# ----------------------------------------------------------------------
sys.stderr.write("verificando objeto %s\n" % "obj1") 
obj1_id = "U-00000001"
obj1 = usuario.busca_por_identificador(obj1_id)
assert obj1 != None
obj1_atrs = usuario.obtem_atributos(obj1)
tabelas.verifica_objeto(usuario, ObjUsuario, obj1, obj1_id, obj1_atrs)
sys.stderr.write("\n")

# !!! Testar obj_para_indice, indice_para_obj, cria_todos_os_testes
