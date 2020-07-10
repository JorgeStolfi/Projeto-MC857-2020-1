#! /usr/bin/python3

import poltrona
import trecho
import compra
import usuario
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
sys.stderr.write("Inicializando módulos, limpando tabela:\n")
compra.inicializa(True)
usuario.inicializa(True)
trecho.inicializa(True)
poltrona.inicializa(True)

# Criando um trecho para teste:
trc1_atrs = \
  { # T-00000001
    'codigo':       "AZ 4036",
    'origem':       "SDU",
    'destino':      "VCP",
    'dia_partida':  "2020-05-09",
    'hora_partida': "19:45",
    'dia_chegada':  "2020-05-09",
    'hora_chegada': "20:40",
    'veiculo':      "AAA-0002",
    'aberto':       True
  }
trc1 = trecho.cria(trc1_atrs)
trc2_atrs = \
  { # T-00000002
    'codigo':       "AZ 4036",
    'origem':       "SDU",
    'destino':      "VCP",
    'dia_partida':  "2020-05-08",
    'hora_partida': "19:45",
    'dia_chegada':  "2020-05-08",
    'hora_chegada': "20:40",
    'veiculo':      "AAA-0002",
    'aberto':       True
  }
trc2 = trecho.cria(trc2_atrs)

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_poltrona(rotulo, pol, ident, atrs):
  """Testes básicos de consistência do objeto {pol} da classe {Objeto_Poltrona}, dados
  {ident} e {atrs} esperados."""
  global ok_global

  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write("verificando poltrona %s\n" % rotulo)
  ok = poltrona.verifica(pol, ident, atrs)

  if pol != None and type(pol) is poltrona.Objeto_Poltrona:
    pass    # Objeto não está com problemas, poltrona é válido
  else:
    ok = False
    erro_prog("algo falhou")

  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("%s\n" % ("-" * 70))
  return

def testa_cria_poltrona(rotulo, ident, atrs):
  """Testa criação de poltrona com atributos com {atrs}. Retorna a poltrona."""
  pol = poltrona.cria(atrs)
  assert poltrona.obtem_identificador(pol) == ident
  assert poltrona.obtem_atributo(pol, 'id_trecho') == atrs['id_trecho'], "epa, trecho errado"
  assert poltrona.obtem_atributo(pol, 'id_compra') == atrs['id_compra'], "epa, pedido de compra errado"
  verifica_poltrona(rotulo, pol, ident, atrs)
  return pol

def testa_lista_livres(trc, trc_id, atrs):
  """Testa retorno da função lista_livres."""
  pol = poltrona.lista_livres(trc)

  livres = [sub['numero'] for sub in atrs if sub['id_trecho'] == trechos[1] and sub['id_compra'] == None]

  ok = (pol == livres)

  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write(trc_id, "ok\n")
  sys.stderr.write("%s\n" % ("-" * 70))
  return livres

# ----------------------------------------------------------------------
sys.stderr.write("testando {poltrona.cria}:\n")

lista_atrs = \
  [
    { 'id_trecho': "T-00000001", 'numero': "01A", 'oferta': True,  'id_compra': "C-00000001", 'preco': 10.00, 'bagagens': 0,    }, # "A-00000001"
    { 'id_trecho': "T-00000001", 'numero': "02A", 'oferta': True,  'id_compra': None,         'preco':  0.00, 'bagagens': None, }, # "A-00000002"
    { 'id_trecho': "T-00000001", 'numero': "02B", 'oferta': False, 'id_compra': "C-00000002", 'preco': 11.00, 'bagagens': 1,    }, # "A-00000003"
    { 'id_trecho': "T-00000002", 'numero': "31",  'oferta': True,  'id_compra': None,         'preco': 50.00, 'bagagens': None, }, # "A-00000004"
    { 'id_trecho': "T-00000002", 'numero': "32",  'oferta': False, 'id_compra': None,         'preco': 20.00, 'bagagens': None, }, # "A-00000005"
    { 'id_trecho': "T-00000002", 'numero': "33",  'oferta': False, 'id_compra': "C-00000001", 'preco': 12.00, 'bagagens': 2,    }, # "A-00000006"
    { 'id_trecho': "T-00000003", 'numero': "31",  'oferta': True,  'id_compra': None,         'preco': 15.00, 'bagagens': None, }, # "A-00000007"
    { 'id_trecho': "T-00000003", 'numero': "33",  'oferta': False, 'id_compra': "C-00000003", 'preco': 13.00, 'bagagens': 3,    }, # "A-00000008"
  ]

pol = [None] * len(lista_atrs)
id_pol = [None] * len(lista_atrs)
pols_next = 1 # Índice da próxima poltrona que não existe na base.
for ind in range(len(lista_atrs)):
  atrs = lista_atrs[ind]
  rot = "%d" % (ind + pols_next)
  id = "A-%08d" % (ind + pols_next)
  pol[ind] = testa_cria_poltrona(rot, id, atrs)
  id_pol[ind] = id

# ----------------------------------------------------------------------
sys.stderr.write("testando {poltrona.muda_atributos}:\n")

pol1 = pol[0]
pol1_id = id_pol[0]
pol1_mods = {
  'numero': "45",
  'id_compra': "C-00000005",
}
poltrona.muda_atributos(pol[0], pol1_mods)
pol1_atrs_m = poltrona.obtem_atributos(pol1)
for k, v in pol1_mods.items():
  pol1_atrs_m[k] = v
verifica_poltrona("pol1_m", pol1, pol1_id, pol1_atrs_m)

# ----------------------------------------------------------------------
sys.stderr.write("testando {poltrona.cria_conjunto}:\n")

trc = trecho.busca_por_identificador('T-00000001')

poltronas = poltrona.cria_conjunto(trc, "001, 05, 5B, 7-10, 12A-15D: 90.50; 04K-6M: 130.00")
print(str(poltronas))

# ----------------------------------------------------------------------
sys.stderr.write("testando {poltrona.obtem_dia_e_hora_de_partida}:\n")
pol3 = pol[3]
assert poltrona.obtem_identificador(pol3) == "A-00000004"
assert poltrona.obtem_atributo(pol3, 'id_trecho') == "T-00000002", "epa, trecho errado"
pol3_dhp_res = poltrona.obtem_dia_e_hora_de_partida(pol3);
pol3_dhp_esp = "2020-05-08 19:45"
if pol3_dhp_res != pol3_dhp_esp:
  sys.stderr.write("{poltrona.obtem_dia_e_hora_de_partida(pol3)}:")
  sys.stderr.write(" devolveu %s, esperado %s\n" % (pol3_dhp_res, pol3_dhp_esp))
  ok = False

# ----------------------------------------------------------------------
sys.stderr.write("testando {poltrona.obtem_dia_e_hora_de_chegada}:\n")
pol3_dhc_res = poltrona.obtem_dia_e_hora_de_chegada(pol3);
pol3_dhc_esp = "2020-05-08 20:40"
if pol3_dhc_res != pol3_dhc_esp:
  sys.stderr.write("{poltrona.obtem_dia_e_hora_de_chegada(pol3)}:")
  sys.stderr.write(" devolveu %s, esperado %s\n" % (pol3_dhc_res, pol3_dhc_esp))
  ok = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
