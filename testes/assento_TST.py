#! /usr/bin/python3

import assento
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
sys.stderr.write("Inicializando módulo {assento}, limpando tabela:\n")
assento.inicializa(True)

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_assento(rotulo, ass, ident, atrs):
  """Testes básicos de consistência do objeto {ass} da classe {Objeto_Assento}, dados
  {ident} e {atrs} esperados."""
  global ok_global

  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write("verificando assento %s\n" % rotulo)
  ok = assento.verifica(ass, ident, atrs)

  if ass != None and type(ass) is assento.Objeto_Assento:
    pass    # Objeto não está com problemas, assento é válido
  else:
    ok = False
    erro_prog("algo falhou")

  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("%s\n" % ("-" * 70))
  return

def testa_cria_assento(rotulo, ident, atrs):
  """Testa criação de assento com atributos com {atrs}. Retorna o assento."""
  ass = assento.cria(atrs)
  verifica_assento(rotulo, ass, ident, atrs)
  return ass

def testa_lista_livres(trc, trc_id, atrs):
  """Testa retorno da função lista_livres."""
  ass = assento.lista_livres(trc)
  livres = [sub['numero'] for sub in atrs if sub['id_trecho'] == trechos[1] and sub['id_compra'] == None]
  ok = (ass == livres)
  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write(trc_id, "ok\n")
  sys.stderr.write("%s\n" % ("-" * 70))
  return

# ----------------------------------------------------------------------
sys.stderr.write("testando {assento.cria}:\n")

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

ass = [None] * len(lista_atrs)
for ind in range(len(lista_atrs)):
  atrs = lista_atrs[ind]
  rot = "%d" % (ind + 1)
  id = "A-%08d" % (ind + 1)
  ass[ind] = testa_cria_assento(rot, id, atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {assento.muda_atributos}:\n")

ass1_mods = {
  'numero': "45",
  'id_compra': "C-00000005",
}
ass1 = ass[0]
ass1_id = "A-00000001"
assento.muda_atributos(ass[0], ass1_mods)
ass1 = ass[0]
ass1_id = "A-00000001"
ass1_d_atrs = lista_atrs[0]
ass1_id = "A-00000001"
ass1 = ass[0]
for k, v in ass1_mods.items():
  ass1_d_atrs[k] = v

ass1 = ass[1]
ass1_id = "C-00000005"
verifica_assento("ass1_d", ass1, ass1_id, ass1_d_atrs)  #

ass2_atrs = lista_atrs[1]
ass2 = ass[1]
if type(ass2) is assento.Objeto_Assento:
  assento.muda_atributos(ass2, ass2_atrs) # Não deveria mudar os atributos
  ass2_id = "A-00000002"
  verifica_assento("ass2", ass2, ass2_id, ass2_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {assento.lista_livres}:\n")

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
