from utils_testes import erro_prog, aviso_prog
import roteiro
import trecho
import sys
import base_sql

"""
Recebe um {rot} e retorna se roterio é realmente uma lista de trechos válidos.
"""

def verifica_roteiro(rot):
    for trc in rot:
        if trc == None or type(trc) is not trecho.Objeto_Trecho:
            return False
    return True

"""
Testa função {descobre_todos} do módulo {roteiros}.
"""
def testa_descobre_todos(origem, destino, dia_min, dia_max):
    try:
        sys.stderr.write("Testando {descobre_todos}\n")
        roteiros = roteiro.descobre_todos(origem, destino, dia_min, dia_max)
        sys.stderr.write("Roteiros retornados:" + str(roteiros) + '\n')
        for rot in roteiros:
            if not verifica_roteiro(rot):
                aviso_prog('{descobre_todos} retornou um {roteiro} com um trecho inválido', True)
    except:
        aviso_prog('Teste da função {descobre_todos} falhou', True)
        return False
    return True

"""
Testa função {obtem_resumo} do módulo {roteiros}.
"""
def testa_obtem_resumo(rot):
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
trecho.cria_testes()


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
ok = ok and testa_descobre_todos('VCP', 'MAO', '2020-05-08', '2020-05-23')

if ok:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("Há erros no módulo {roteiro}")
