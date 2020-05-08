#! /usr/bin/python3

import objeto
import tabela_generica
import tabelas
import base_sql
import identificador
import utils_testes
import conversao_sql
import sys
from utils_testes import erro_prog, aviso_prog, mostra

# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
base_sql.conecta("DB", None, None)

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

# ----------------------------------------------------------------------
# Classe de objeto para teste:

class ObjTeste(objeto.Objeto):
  
  def __init__(self, id, atrs):
    objeto.Objeto.__init__(self, id, atrs)

obj0 = ObjTeste("X-00000000", { }) # An object just to get its type

# ----------------------------------------------------------------------
sys.stderr.write("tabela para teste:\n")

nome_tb = "objtestes"

letra_tb = "X"
  # Prefixo dos identificadores de testes

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {ObjTeste} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidade dos objetos.

colunas = \
  (
    ( 'coisa',         type(100),   'INTEGER', False ),
    ( 'treco',         type(100),   'INTEGER', False ),
    ( 'lhufas',        type("foo"), 'TEXT',    False ),
  )
  # Descrição das colunas da tabela na base de dados.
 
tabela_generica.limpa_tabela(nome_tb, colunas)

# ----------------------------------------------------------------------
def def_obj_mem(obj, id, atrs_SQL):
  """Função que cria ou modifica objeto na memória."""
  global cache, nome_tb, letra_tb, colunas, diags
  if obj == None:
    atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, False, tabelas.id_para_objeto)
    obj = ObjTeste(id, atrs_mem)
  else:
    assert obj.id == id
    mods_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, True, tabelas.id_para_objeto)
    # Modifica os atributos:
    for chave, val in mods_mem.items():
      val_velho = obj.atrs[chave]
      obj.atrs[chave] = val
  return obj

# ----------------------------------------------------------------------
# Funções auxiliares de teste

def verifica_objeto(rotulo, obj, id, atrs):
  """Testes básicos de consistência do objeto {obj} da classe {ObjTeste}, dados 
  {id} e {atrs} esperados."""
  global ok_global

  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write("verificando usuário %s\n" % rotulo)
  ok = objeto.verifica(obj, type(obj0), id, atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem)

  if not ok:
    aviso_prog("teste falhou", True)
    ok_global = False

  sys.stderr.write("%s\n" % ("-" * 70))
  return
 
def testa_cria_objeto(rotulo, id, atrs):
  """Testa criação de objeto com atributos com {atrs}. Retorna o usuário."""
  obj = objeto.cria(atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  verifica_objeto(rotulo, obj, id, atrs)
  return obj

# ----------------------------------------------------------------------
sys.stderr.write("testando {objeto.cria}:\n")
obj1_atrs = { 'coisa': 100, 'treco': 101, 'lhufas': "cem" }
obj1_ind = 1
obj1_id = ("X-%08d" % obj1_ind)
obj1 = testa_cria_objeto("obj1", obj1_id, obj1_atrs)

obj2_atrs = { 'coisa': 200, 'treco': 201, 'lhufas': "duzentos" }
obj2_ind = 2
obj2_id = ("X-%08d" % obj2_ind)
obj2 = testa_cria_objeto("obj2", obj2_id, obj2_atrs)

obj3_atrs = { 'coisa': 300, 'treco': 301, 'lhufas': "trezentos" }
obj3_ind = 3
obj3_id = ("X-%08d" % obj3_ind)
obj3 = testa_cria_objeto("obj3", obj3_id, obj3_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {objeto.muda_atributos}:\n")

obj1_mods = {
  'coisa': 109,
  'lhufas': "cento e nove"
}
objeto.muda_atributos(obj1, obj1_mods, cache, nome_tb, letra_tb, colunas, def_obj_mem)
obj1_atrs_m = obj1_atrs
for k, v in obj1_mods.items():
  obj1_atrs_m[k] = v
verifica_objeto("obj1_d", obj1, obj1_id, obj1_atrs_m)

objeto.muda_atributos(obj2, obj2_atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem) # Não deveria mudar os atributos
verifica_objeto("obj2", obj2, obj2_id, obj2_atrs)

obj2_atrs_m = obj3_atrs.copy()
objeto.muda_atributos(obj2, obj2_atrs_m, cache, nome_tb, letra_tb, colunas, def_obj_mem) # Deveria assumir os valores do obj3
verifica_objeto("obj2_m", obj2, obj2_id, obj2_atrs_m)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
