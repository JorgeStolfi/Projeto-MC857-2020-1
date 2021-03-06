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
    'encerrado':   False
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
    'encerrado':    False
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

polt1 = { 'id_trecho': "T-00000001", 'numero': "01A", 'oferta': True,  'id_compra': "C-00000001", \
          'preco': 10.00, 'bagagens': 0, 'fez_checkin': True} # "A-00000001"

polt2 = { 'id_trecho': "T-00000001", 'numero': "02A", 'oferta': True,  'id_compra': None, \
          'preco':  0.00, 'bagagens': None, 'fez_checkin': True} # "A-00000002"

polt3 = { 'id_trecho': "T-00000001", 'numero': "02B", 'oferta': False, 'id_compra': "C-00000002", \
          'preco': 11.00, 'bagagens': 1, 'fez_checkin': True} # "A-00000003"

polt4 = { 'id_trecho': "T-00000002", 'numero': "31",  'oferta': True,  'id_compra': None, \
          'preco': 50.00, 'bagagens': None, 'fez_checkin': True} # "A-00000004"

polt5 = { 'id_trecho': "T-00000002", 'numero': "32",  'oferta': False, 'id_compra': None, \
          'preco': 20.00, 'bagagens': None, 'fez_checkin': False} # "A-00000005"

polt6 = { 'id_trecho': "T-00000002", 'numero': "33",  'oferta': False, 'id_compra': "C-00000001", \
          'preco': 12.00, 'bagagens': 2, 'fez_checkin': False} # "A-00000006"

polt7 = { 'id_trecho': "T-00000003", 'numero': "31",  'oferta': True,  'id_compra': None, \
          'preco': 15.00, 'bagagens': None, 'fez_checkin': False} # "A-00000007"

polt8 = { 'id_trecho': "T-00000003", 'numero': "33",  'oferta': False, 'id_compra': "C-00000003", \
          'preco': 13.00, 'bagagens': 3, 'fez_checkin': False} # "A-00000008"

lista_atrs = [ polt1, polt2, polt3, polt4, polt5, polt6, polt7, polt8]

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
sys.stderr.write("testando {poltrona.resume_numeros_e_precos}:\n")

lista_de_pares1 = [('2', '90.50'), ('4B', '20.30'), ('6A', '30.50'), ('1122', '90.50')]
lista_de_pares2 = [('10B', '100'), ('1B', '100'), ('3B', '100'), ('1', '20.0')]
lista_de_pares3 = [('1', '10.0'), ('2', '20.0'), ('3', '30.0')]

representacao_str1 = poltrona.resume_numeros_e_precos(lista_de_pares1)
representacao_str2 = poltrona.resume_numeros_e_precos(lista_de_pares2)
representacao_str3 = poltrona.resume_numeros_e_precos(lista_de_pares3)

sys.stderr.write(representacao_str1 + "\n")
sys.stderr.write(representacao_str2 + "\n")
sys.stderr.write(representacao_str3 + "\n")

# ----------------------------------------------------------------------
sys.stderr.write("testando {poltrona.obtem_dia_e_hora_de_partida}:\n")
pol3 = pol[3]
assert poltrona.obtem_identificador(pol3) == "A-00000004"
assert poltrona.obtem_atributo(pol3, 'id_trecho') == "T-00000002", "epa, trecho errado"
pol3_dhp_res = poltrona.obtem_dia_e_hora_de_partida(pol3);
pol3_dhp_esp = "2020-05-08 19:45 UTC"
if pol3_dhp_res != pol3_dhp_esp:
  sys.stderr.write("{poltrona.obtem_dia_e_hora_de_partida(pol3)}:")
  sys.stderr.write(" devolveu %s, esperado %s\n" % (pol3_dhp_res, pol3_dhp_esp))
  ok_global = False

# ----------------------------------------------------------------------
sys.stderr.write("testando {poltrona.obtem_dia_e_hora_de_chegada}:\n")
pol3_dhc_res = poltrona.obtem_dia_e_hora_de_chegada(pol3);
pol3_dhc_esp = "2020-05-08 20:40 UTC"
if pol3_dhc_res != pol3_dhc_esp:
  sys.stderr.write("{poltrona.obtem_dia_e_hora_de_chegada(pol3)}:")
  sys.stderr.write(" devolveu %s, esperado %s\n" % (pol3_dhc_res, pol3_dhc_esp))
  ok_global = False

# ----------------------------------------------------------------------
sys.stderr.write("---------------------------------------------\n")
sys.stderr.write("testando {poltrona.obtem_numeros_e_precos}:\n\n")

# O esperado para 'A-00000001' é 45 poi o valor é mudado nos testes das linha 131 a 143, de {poltrona.muda_atributos}
ids_poltronas = ["A-00000001", "A-00000003", "A-00000005", "A-00000007"]
esperado = [("45", 10.00), ("02B", 11.00), ("32", 20.00), ("31", 15.00)]

res = poltrona.obtem_numeros_e_precos(ids_poltronas)
if res != esperado:
  sys.stderr.write(" devolveu {}, esperado {}\n".format(res, esperado))
  ok_global = False

res = poltrona.obtem_numeros_e_precos(ids_poltronas[:1])
if res != esperado[:1]:
  sys.stderr.write(" devolveu {}, esperado {}\n".format(res, esperado[:1]))
  ok_global = False

res = poltrona.obtem_numeros_e_precos(ids_poltronas[1:3])
if res != esperado[1:3]:
  sys.stderr.write(" devolveu {}, esperado {}\n".format(res, esperado[1:3]))
  ok_global = False

res = poltrona.obtem_numeros_e_precos(ids_poltronas[1:])
if res != esperado[1:]:
  sys.stderr.write(" devolveu {}, esperado {}\n".format(res, esperado[1:]))
  ok_global = False
  
sys.stderr.write("---------------------------------------------\n")

# ----------------------------------------------------------------------
sys.stderr.write("testando {poltrona.livre_mais_proxima}:\n")

polt_res = poltrona.livre_mais_proxima(pol[1], 95.0)
id_res = poltrona.obtem_identificador(polt_res)
sys.stderr.write("Devolveu a poltrona de id %s\n" % id_res)
sys.stderr.write("Ainda e necessario implementar poltrona.dist\n")
polt_res_esp = "Ainda e necessario implementar poltrona.dist"
if polt_res == None: # Mesmo com a distancia aleatoria a resposta nao pode ser None com um preco max de 95 pois ha poltronas livres por 90.5
  sys.stderr.write(" devolveu %s, esperado %s\n" % (polt_res, 'algo diferente de None'))
  ok_global = False
  
  
  
sys.stderr.write("---------------------------------------------\n")

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
