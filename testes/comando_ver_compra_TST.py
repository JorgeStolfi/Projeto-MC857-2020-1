import sys
import comando_ver_compra
import html_pag_mensagem_de_erro
import base_sql
import tabelas
import usuario
import sessao
import compra
import utils_testes; from utils_testes import erro_prog, mostra

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando objetos...\n")
tabelas.cria_todos_os_testes(False)

id_compra = "C-00000001"

ses = sessao.busca_por_identificador("S-00000001")
usr = usuario.busca_por_identificador("U-00000003")
compra = compra.busca_por_identificador(id_compra)

if compra:
  sys.stderr.write("Compra encontrada\n")
  args = { 'id_usuario': id, "id_compra": compra.id}
else:
  erro_prog("comando_ver_compra_TST : teste falhou : compra nao encontrada")


def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = comando_ver_compra
  funcao = modulo.processa
  frag = False
  pretty = False
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa('compra_existente', ses, args)
