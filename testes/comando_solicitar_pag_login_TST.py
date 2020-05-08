import comando_solicitar_pag_login
import base_sql
import tabelas
import usuario
import sessao
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

ses = sessao.busca_por_identificador("S-00000001")
args = {'coisa': True}

html = comando_solicitar_pag_login.processa(ses, args)
html = html + "\n"
