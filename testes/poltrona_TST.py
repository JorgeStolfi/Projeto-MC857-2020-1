#! /usr/bin/python3

import poltrona
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
sys.stderr.write("Inicializando módulo {poltrona}, limpando tabela:\n")
poltrona.inicializa(True)

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_poltrona(rotulo, pol, ident, atrs):
  """Testes básicos de consistência do objeto {pol} da classe {Objeto_Poltrona}, dados
  {ident} e {atrs} esperados."""
  global ok_global

  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write("verificanda poltrona %s\n" % rotulo)
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
    { 'id_trecho': "T-00000001", 'numero': "01A", 'oferta': True,  'id_compra': "C-00000001", 'preco': "10", 'bagagens': 0,    },
    { 'id_trecho': "T-00000001", 'numero': "02A", 'oferta': True,  'id_compra': None,         'preco': "0",  'bagagens': None, },
    { 'id_trecho': "T-00000001", 'numero': "02B", 'oferta': False, 'id_compra': "C-00000002", 'preco': "11", 'bagagens': 1,    },
    { 'id_trecho': "T-00000002", 'numero': "31",  'oferta': True,  'id_compra': None,         'preco': "0",  'bagagens': None, },
    { 'id_trecho': "T-00000002", 'numero': "32",  'oferta': False, 'id_compra': None,         'preco': "0",  'bagagens': None, },
    { 'id_trecho': "T-00000002", 'numero': "33",  'oferta': False, 'id_compra': "C-00000001", 'preco': "12", 'bagagens': 2,    },
    { 'id_trecho': "T-00000003", 'numero': "31",  'oferta': True,  'id_compra': None,         'preco': "0",  'bagagens': None, },
    { 'id_trecho': "T-00000003", 'numero': "33",  'oferta': False, 'id_compra': "C-00000003", 'preco': "13", 'bagagens': 3,    },
  ]

pol = [None] * len(lista_atrs)
for ind in range(len(lista_atrs)):
  atrs = lista_atrs[ind]
  rot = "%d" % (ind + 1)
  id = "A-%08d" % (ind + 1)
  pol[ind] = testa_cria_poltrona(rot, id, atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {poltrona.muda_atributos}:\n")

pol1_mods = {
  'numero': "45",
  'id_compra': "C-00000005",
}
pol1 = pol[0]
pol1_id = "A-00000001"
poltrona.muda_atributos(pol[0], pol1_mods)
pol1 = pol[0]
pol1_id = "A-00000001"
pol1_d_atrs = lista_atrs[0]
pol1_id = "A-00000001"
pol1 = pol[0]
for k, v in pol1_mods.items():
  pol1_d_atrs[k] = v

pol1 = pol[1]
pol1_id = "C-00000005"
verifica_poltrona("pol1_d", pol1, pol1_id, pol1_d_atrs)  #

pol2_atrs = lista_atrs[1]
pol2 = pol[1]
if type(pol2) is poltrona.Objeto_Poltrona:
  poltrona.muda_atributos(pol2, pol2_atrs) # Não deveria mudar os atributos
  pol2_id = "A-00000002"
  verifica_poltrona("pol2", pol2, pol2_id, pol2_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {poltrona.lista_livres}:\n")

# Listando ids de trechos existentes na lista_atrs
trechos = list(set([sub['id_trecho'] for sub in lista_atrs]))
trechos.sort()
for trc_id in trechos:
  trc = trecho.busca_por_identificador(trc_id)
  testa_lista_livres(trc, trc_id, lista_atrs)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
