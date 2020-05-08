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
sys.stderr.write("Inicializando módulo {assento}, criando testes:\n")
assento.inicializa(True)
assento.cria_testes()

ass1 = assento.busca_por_identificador("A-00000001")
ass2 = assento.busca_por_identificador("A-00000002")
ass3 = assento.busca_por_identificador("A-00000003")
ass4 = assento.busca_por_identificador("A-00000004")
ass5 = assento.busca_por_identificador("A-00000005")
ass6 = assento.busca_por_identificador("A-00000006")

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
    if ident1 != ident:
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
 
# ----------------------------------------------------------------------
sys.stderr.write("testando {trecho.cria}:\n")

trc1_atrs = {
  'codigo':      "AZ 4024",
  'origem':      "VCP",
  'destino':     "SDU",
  'dt_partida':  "2020-05-08 12:45"
  'dt_chegada':  "2020-05-08 13:40"
  'assentos':    [ ass1, ass2, ass3, ]
}
trc1_ind = 1
trc1_id = "T-00000001"
trc1 = testa_cria_trecho("trc1", trc1_id, trc1_atrs)

trc2_atrs = {
  'codigo':      "AZ 4036",
  'origem':      "SDU",
  'destino':     "VCP",
  'dt_partida':  "2020-05-08 19:45"
  'dt_chegada':  "2020-05-08 20:40"
  'assentos':    [ ass4, ass5, ass6, ]
}
trc2_ind = 2
trc2_id = "T-00000002"
trc2 = testa_cria_trecho("trc2", trc2_id, trc2_atrs)

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
