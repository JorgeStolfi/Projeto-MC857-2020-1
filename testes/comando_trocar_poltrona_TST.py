import sys
import comando_trocar_poltrona
import base_sql
import tabelas
import sessao
import compra
import poltrona
import trecho
from utils_testes import erro_prog, testa_gera_html

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando objetos...\n")
tabelas.cria_todos_os_testes()

ses = sessao.busca_por_identificador("S-00000003")
trc = trecho.busca_por_identificador("T-00000003")

pag = comando_trocar_poltrona.processa(ses, "A-00000008", trc, "C-00000003")
sys.stderr.write(str(pag))