from utils_testes import erro_prog, aviso_prog
import roteiro
import trecho
import sys
import base_sql


def verifica_roteiro(rot):
  """
  Recebe um {rot} e retorna se roterio é realmente uma lista de trechos válidos.
  """
  for trc in rot:
    if trc == None or type(trc) is not trecho.Objeto_Trecho:
      return False
  return True

def testa_obtem_resumo(rot):
  """
  Testa função {obtem_resumo} do módulo {roteiros}.
  """
  try:
    sys.stderr.write("Testando {obtem_resumo}\n")
    resumo = roteiro.obtem_resumo(rot)
    sys.stderr.write("Resumo retornado:" + str(resumo) + '\n')
  except:
    aviso_prog('Teste da função {obtem_resumo} falhou',True)
    return False
  return True

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)

trecho.inicializa(False)
trecho.cria_testes(False)

sys.stderr.write("----------" * 7 + "\n")
sys.stderr.write("Testando {roteiro.obtem_resumo}\n")

trc_VCP_SDU_1 = trecho.busca_por_identificador("T-00000001")
trc_VCP_SDU_2 = trecho.busca_por_identificador("T-00000002")
trc_SDU_POA_1 = trecho.busca_por_identificador("T-00000004")
trc_POA_MAO_1 = trecho.busca_por_identificador("T-00000005")
trc_SDU_MAO_1 = trecho.busca_por_identificador("T-00000006")
rot1 = [ trc_VCP_SDU_1, trc_SDU_POA_1, trc_POA_MAO_1]
rot2 = [ trc_VCP_SDU_1, trc_SDU_MAO_1 ]
rot3 = [ trc_VCP_SDU_2, trc_SDU_MAO_1 ]

ok = True
ok = ok and testa_obtem_resumo(rot1)
ok = ok and testa_obtem_resumo(rot2)
ok = ok and testa_obtem_resumo(rot3)

sys.stderr.write("----------" * 7 + "\n")
sys.stderr.write("Testando {roteiro.descobre_todos}\n")

def testa_descobre_todos(origem, destino, data_min, data_max, soh_disponiveis):
  """
  Testa função {descobre_todos} do módulo {roteiros}.
  """
  tx_args = "'%s', '%s', '%s', '%s', %s" % (origem, destino, data_min, data_max, str(soh_disponiveis))
  sys.stderr.write("Testando {descobre_todos}(%s)\n" % tx_args)
  roteiros = roteiro.descobre_todos(origem, destino, data_min, data_max, soh_disponiveis)
  sys.stderr.write("Roteiros retornados:\n")
  ok_local = True
  for rot in roteiros:
    sys.stderr.write("  " + str(roteiros) + "\n")
    if not verifica_roteiro(rot):
      aviso_prog('** roteiro inválido', True)
      ok_local = False
  return ok_local

origem = "VCP"
data_min = "2020-05-08 08:00 UTC"
destino = "MAO"
data_max = "2020-05-23 18:00 UTC"
soh_disponiveis = False

ok = ok and testa_descobre_todos(origem, data_min, destino, data_max, soh_disponiveis)

if ok:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("Há erros no módulo {roteiro}")
