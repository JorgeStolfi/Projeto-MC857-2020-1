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
    dia1 = atrs['dia_partida']
    hora1 = atrs['hora_partida']
    trc1 = trecho.busca_por_codigo_e_data(cod1, dia1, hora1)
    if trc1 != trc:
      aviso_prog("retornou " + str(trc1) + ", deveria ter retornado " + str(trc),True)
      ok = False

  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("%s\n" % ("-" * 70))
  return

def testa_cria_trecho(rotulo, ident, atrs):
  """Testa criação de trecho com atributos {atrs}.  Retorna o trecho."""
  sys.stderr.write("  %s %s" % (ident, atrs['codigo']));
  sys.stderr.write("  %s %s %s" % (atrs['origem'], atrs['dia_partida'], atrs['hora_partida']))
  sys.stderr.write("  %s %s %s" % (atrs['destino'], atrs['dia_chegada'], atrs['hora_chegada']))
  sys.stderr.write("\n")
  trc = trecho.cria(atrs)
  verifica_trecho(rotulo, trc, ident, atrs)
  return trc

def testa_busca_por_origem(cod, ids):
  """ Testa a função {trecho.busca_por_origem} com parâmetro {cod},
  que deve retornar a lista de indentificadores de trechos {ids}."""
  global ok_global
   # ----------------------------------------------------------------------
  sys.stderr.write("testando {busca_por_origem()}:\n")
  ids1 = trecho.busca_por_origem(cod)
  if ids1 != ids:
    aviso_prog("retornou " + str(ids1) + ", deveria ter retornado " + str(ids),True)
    ok_global = False

  return

def testa_busca_por_dias(dia_min, dia_max, ids):
  """ Testa a função {trecho.busca_por_dias} com parâmetros
  {dia_min,dia_max}, que deve retornar a lista de indentificadores
  de trechos {ids}."""
  global ok_global
   # ----------------------------------------------------------------------
  sys.stderr.write("testando {busca_por_dias()}:\n")
  ids1 = trecho.busca_por_dias(dia_min, dia_max)
  if ids1 != ids:
    aviso_prog("retornou " + str(ids1) + ", deveria ter retornado " + str(ids),True)
    ok_global = False

  return

def testa_busca_por_origem_e_destino(org, dst, data_min, data_max, ids):
  """ Testa a função {trecho.busca_por_origem_e_destino} com parâmetros
  {org, dst, dia_min,dia_max}, que deve retornar a lista de indentificadores
  de trechos {ids}."""
  global ok_global
  # ----------------------------------------------------------------------
  sys.stderr.write("testando {busca_por_origem_e_destino()}:\n")
  ids1 = trecho.busca_por_origem_e_destino(org, dst, data_min, data_max)
  if ids1 != ids:
    aviso_prog("retornou " + str(ids1) + ", deveria ter retornado " + str(ids),True)
    ok_global = False

# ----------------------------------------------------------------------
sys.stderr.write("testando {trecho.cria}:\n")

trc1_atrs = {
  'codigo':       "AZ 4024",
  'origem':       "VCP",
  'destino':      "SDU",
  'dia_partida':  "2020-05-08",
  'hora_partida': "12:45",
  'dia_chegada':  "2020-05-08",
  'hora_chegada': "13:40",
  'veiculo':      "PP-CAI",
  'aberto':       True,
}
trc1_ind = 1
trc1_id = "T-00000001"
trc1 = testa_cria_trecho("trc1", trc1_id, trc1_atrs)

trc2_atrs = {
  'codigo':       "AZ 4036",
  'origem':       "SDU",
  'destino':      "VCP",
  'dia_partida':  "2020-05-08",
  'hora_partida': "19:45",
  'dia_chegada':  "2020-05-08",
  'hora_chegada': "20:40",
  'veiculo':      "PP-BUM",
  'aberto':       True,
}
trc2_ind = 2
trc2_id = "T-00000002"
trc2 = testa_cria_trecho("trc2", trc2_id, trc2_atrs)

trc3_atrs = {
  'codigo':       "AZ 4036",
  'origem':       "SDU",
  'destino':      "VCP",
  'dia_partida':  "2020-05-09",
  'hora_partida': "19:45",
  'dia_chegada':  "2020-05-09",
  'hora_chegada': "20:40",
  'veiculo':      "PP-PAU",
  'aberto':       True,
}
trc3_ind = 2
trc3_id = "T-00000003"
trc3 = testa_cria_trecho("trc3", trc3_id, trc3_atrs)

trc4_atrs = {
  'codigo':       "BU 2115",
  'origem':       "MAO",
  'destino':      "VCP",
  'dia_partida':  "2020-05-07",
  'hora_partida': "17:15",
  'dia_chegada':  "2020-05-08",
  'hora_chegada': "07:70",
  'veiculo':      "PQ-NAO",
  'aberto':       True,
}
trc4_ind = 3
trc4_id = "T-00000004"
trc4 = testa_cria_trecho("trc4", trc4_id, trc4_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {trecho.busca_por_dias}\n")
dia_min_bd1 = "2020-05-08"
dia_max_bd1 = "2020-05-09"
sys.stderr.write("buscando %s .. %s:\n" % (dia_min_bd1, dia_max_bd1))
ids_bd1 = [trc1_id, trc2_id, trc3_id]
testa_busca_por_dias(dia_min_bd1, dia_max_bd1, ids_bd1)

dia_min_bd2 = "2020-05-06"
dia_max_bd2 = "2020-05-08"
sys.stderr.write("buscando %s .. %s:\n" % (dia_min_bd2, dia_max_bd2))
ids_bd2 = [trc1_id, trc2_id, trc4_id]
testa_busca_por_dias(dia_min_bd2, dia_max_bd2, ids_bd2)

sys.stderr.write("%s\n" % ("-" * 70))

# ----------------------------------------------------------------------
sys.stderr.write("testando {trecho.busca_por_origem_e_destino}:\n")
org_bod1 = "SDU"
data_min_bod1 = "2020-05-08 00:00 UTC"
dst_bod1 = "VCP"
data_max_bod1 = "2020-05-08 23:59 UTC"
sys.stderr.write("buscando (%s %s) .. (%s %s):\n" % (str(org_bod1), data_min_bod1, str(dst_bod1), data_max_bod1))
ids_bod1 = [trc2_id]
testa_busca_por_origem_e_destino(org_bod1, dst_bod1, data_min_bod1, data_max_bod1, ids_bod1)

org_bod2 = None
data_min_bod2 = "2020-05-08 00:00 UTC"
dst_bod2 = "VCP"
data_max_bod2 = "2020-05-09 23:59 UTC"
sys.stderr.write("buscando (%s %s) .. (%s %s):\n" % (str(org_bod2), data_min_bod2, str(dst_bod2), data_max_bod2))
ids_bod2 = [trc2_id, trc3_id]
testa_busca_por_origem_e_destino(org_bod2, dst_bod2, data_min_bod2, data_max_bod2, ids_bod2)

org_bod3 = "VCP"
data_min_bod3 = None
dst_bod3 = None
data_max_bod3 = "2020-05-08 23:59 UTC"
ids_bod3 = [trc1_id]
sys.stderr.write("buscando (%s %s) .. (%s %s):\n" % (str(org_bod3), data_min_bod3, str(dst_bod3), data_max_bod3))
testa_busca_por_origem_e_destino(org_bod3, dst_bod3, data_min_bod3, data_min_bod3, ids_bod3)

# ----------------------------------------------------------------------
sys.stderr.write("testando {trecho.busca_por_origem}:\n")
origem = 'VCP'
ids_ori_bd1 = [trc1_id]
testa_busca_por_origem(origem, ids_ori_bd1)

origem = 'SDU'
ids_ori_bd1 = [trc2_id, trc3_id]
testa_busca_por_origem(origem, ids_ori_bd1)

# ----------------------------------------------------------------------
sys.stderr.write("testando {trecho.muda_atributos}:\n")

# Testando troca de alguns atributos:
trc1_mods = {
  'codigo':       "GO 2331",
  'dia_partida':  "2020-05-08",
  'hora_partida': "12:33",
  'veiculo':      "PU-MBA",
  'aberto':       False
}
trecho.muda_atributos(trc1, trc1_mods)
trc1_atrs_m = trc1_atrs
for k, v in trc1_mods.items():
  trc1_atrs_m[k] = v
verifica_trecho("trc1_m", trc1, trc1_id, trc1_atrs_m)

# Testando troca de todos os atributos pelos mesmos valores.
trc2_mods = trc2_atrs.copy()
trc2_atrs_m = trc2_atrs.copy()
trecho.muda_atributos(trc2, trc2_mods) # Não deveria mudar os atributos
verifica_trecho("trc2", trc2, trc2_id, trc2_atrs_m)

# Testando troca de todos os atributos por outros valores.
trc3_mods = trc2_atrs.copy() 
trc3_mods['dia_partida'] = "2020-05-10" # Para evitar duplicação de {(cod,dia,hora)}
trc3_mods['aberto'] = False
trc3_atrs_m = trc3_mods.copy()
trecho.muda_atributos(trc3, trc3_mods) # Deveria assumir os valores do trc3
verifica_trecho("trc3_m", trc3, trc3_id, trc3_atrs_m)

# ----------------------------------------------------------------------
sys.stderr.write("testando {trecho.obtem_dia_e_hora_de_partida}:\n")
trc2_dhp_res = trecho.obtem_dia_e_hora_de_partida(trc2);
trc2_dhp_esp = "2020-05-08 19:45 UTC"
if trc2_dhp_res != trc2_dhp_esp:
  sys.stderr.write("{trecho.obtem_dia_e_hora_de_partida(trc2)}:")
  sys.stderr.write(" devolveu %s, esperado %s\n" % (trc2_dhp_res, trc2_dhp_esp))
  ok = False

# ----------------------------------------------------------------------
sys.stderr.write("testando {trecho.obtem_dia_e_hora_de_chegada}:\n")
trc2_dhc_res = trecho.obtem_dia_e_hora_de_chegada(trc2);
trc2_dhc_esp = "2020-05-08 20:40 UTC"
if trc2_dhc_res != trc2_dhc_esp:
  sys.stderr.write("{trecho.obtem_dia_e_hora_de_chegada(trc2)}:")
  sys.stderr.write(" devolveu %s, esperado %s\n" % (trc2_dhc_res, trc2_dhc_esp))
  ok = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
