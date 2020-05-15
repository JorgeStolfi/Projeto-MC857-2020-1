#! /usr/bin/python3

import trecho
import tabela_generica
import base_sql
import identificador
import utils_testes
import sys
from utils_testes import erro_prog, aviso_prog, mostra

# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
base_sql.conecta("DB",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("Inicializando módulo {trecho}, limpando tabela:\n")
trecho.inicializa(True)

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_trecho(rotulo, trc, ident, atrs):
  """Testes básicos de consistência do objeto {trc} da classe {Objeto_Trecho}, dados 
  {ident} e {atrs} esperados."""
  global ok_global

  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write("verificando trecho %s\n" % rotulo)
  ok = trecho.verifica(trc, ident, atrs)

  if trc != None and type(trc) is trecho.Objeto_Trecho:
    
    # ----------------------------------------------------------------------
    sys.stderr.write("testando {busca_por_codigo_e_data()}:\n")
    cod1 = atrs['codigo']
    dt1 = atrs['dt_partida']
    ident1 = trecho.busca_por_codigo_e_data(cod1, dt1)
    if ident1 != [ ident ]:
      aviso_prog("retornou " + str(ident1) + ", deveria ter retornado " + str(ident),True)
      ok = False

  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("%s\n" % ("-" * 70))
  return
 
def testa_cria_trecho(rotulo, ident, atrs):
  """Testa criação de trecho com atributos com {atrs}. Retorna o trecho."""
  trc = trecho.cria(atrs)
  verifica_trecho(rotulo, trc, ident, atrs)
  return trc
 
def test_busca_por_origem(cod):
  erro_prog("Função {objeto.busca_por_campo} não implementada")
  return

# ----------------------------------------------------------------------
sys.stderr.write("testando {trecho.cria}:\n")

trc1_atrs = {
  'codigo':      "AZ 4024",
  'origem':      "VCP",
  'destino':     "SDU",
  'dt_partida':  "2020-05-08 12:45",
  'dt_chegada':  "2020-05-08 13:40",
}
trc1_ind = 1
trc1_id = "T-00000001"
trc1 = testa_cria_trecho("trc1", trc1_id, trc1_atrs)

trc2_atrs = {
  'codigo':      "AZ 4036",
  'origem':      "SDU",
  'destino':     "VCP",
  'dt_partida':  "2020-05-08 19:45",
  'dt_chegada':  "2020-05-08 20:40",
}
trc2_ind = 2
trc2_id = "T-00000002"
trc2 = testa_cria_trecho("trc2", trc2_id, trc2_atrs)

trc3_atrs = {
  'codigo':      "AZ 4036",
  'origem':      "SDU",
  'destino':     "VCP",
  'dt_partida':  "2020-05-09 19:45",
  'dt_chegada':  "2020-05-09 20:40",
}
trc3_ind = 2
trc3_id = "T-00000003"
trc3 = testa_cria_trecho("trc3", trc3_id, trc3_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {trecho.muda_atributos}:\n")

trc1_mods = {
  'codigo': "GO 2331",
  'dt_partida': "2020-05-08 12:33",
}
trecho.muda_atributos(trc1, trc1_mods)
trc1_d_atrs = trc1_atrs
for k, v in trc1_mods.items():
  trc1_d_atrs[k] = v
verifica_trecho("trc1_d", trc1, trc1_id, trc1_d_atrs)

if type(trc2) is trecho.Objeto_Trecho:
  trecho.muda_atributos(trc2, trc2_atrs) # Não deveria mudar os atributos
  verifica_trecho("trc2", trc2, trc2_id, trc2_atrs)

if type(trc2) is trecho.Objeto_Trecho:
  trc2_m_atrs = trc3_atrs.copy()
  trecho.muda_atributos(trc2, trc2_m_atrs) # Deveria assumir os valores do trc3
  verifica_trecho("trc2_m", trc2, trc2_id, trc2_m_atrs)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
