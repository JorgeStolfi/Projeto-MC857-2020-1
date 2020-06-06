import sys
import comando_ver_minhas_compras
import base_sql
import tabelas
import usuario
import sessao
import compra
from utils_testes import erro_prog, mostra

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando objetos...\n")
tabelas.cria_todos_os_testes()

# !! CONSERTAR !!!

ses = sessao.busca_por_identificador("S-00000001")
id = usuario.busca_por_identificador("U-00000001")

args = { 'id_usuario': id }
userTest = comando_ver_minhas_compras.processa(ses, args)

if userTest == id :
  sys.stderr.write("Nao houve erros\n")
else:
  erro_prog(" : teste falhou")
