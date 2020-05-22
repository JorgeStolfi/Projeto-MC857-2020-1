# Implementação do módulo {objeto} e da classe {Objeto}.

import objeto

import tabela_generica
import conversao_sql
import sys
import identificador
import valida_campo; from valida_campo import ErroAtrib

import sys # Para diagnóstico.
from utils_testes import erro_prog, aviso_prog, mostra

# VARIÁVEIS GLOBAIS DO MÓDULO
  
diags = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

class Objeto_IMP:

  def __init__(self, id, atrs):
    self.id = id
    self.atrs = atrs.copy()

# Implementação das funções:

def cria(atrs_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem):
  global diags
  if diags: mostra(0,"objeto_IMP.cria(" + str(atrs_mem) + ") ...")

  # Converte atibutos para formato SQL.
  atrs_SQL = conversao_sql.dict_mem_para_dict_SQL(atrs_mem, colunas, False)
  # Insere na base de dados e obtém o índice na mesma:
  obj = tabela_generica.acrescenta(nome_tb, cache, letra_tb, colunas, def_obj_mem, atrs_SQL)
  return obj

def muda_atributos(obj, mods_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem):
  global diags

  # Converte valores de formato memória para formato SQL.
  mods_SQL = conversao_sql.dict_mem_para_dict_SQL(mods_mem, colunas, True)
  res = tabela_generica.atualiza(nome_tb, cache, letra_tb, colunas, def_obj_mem, obj.id, mods_SQL)
  assert res == obj
  return

def obtem_identificador(obj):
  global diags
  return obj.id

def obtem_atributos(obj):
  global diags
  return obj.atrs.copy()

def obtem_atributo(obj, chave):
  global diags
  return obj.atrs[chave]

def busca_por_identificador(id, cache, nome_tb, letra_tb, colunas, def_obj_mem):
  global diags
  obj = tabela_generica.busca_por_identificador(nome_tb, cache, letra_tb, colunas, def_obj_mem, id)
  return obj

def busca_por_campo(chave, val, unico, cache, nome_tb, letra_tb, colunas):
  global diags
  ids = tabela_generica.busca_por_campo(nome_tb, letra_tb, colunas, chave, val, None)
  if unico:
    return identificador.unico_elemento(ids)
  else:
    return ids
    
def busca_por_campos(args, unico, cache, nome_tb, letra_tb, colunas):
  global diags
  res = tabela_generica.busca_por_campos(nome_tb, letra_tb, colunas, args, None)
  if res == None: res = [].copy() # Just in case.
  if type(res) is list or type(res) is tuple:
    return res
  elif type(res) is str:
    erro_prog("busca na tabela falhou, res = " + res)
  else:
    erro_prog("busca na tabela devolveu resultado inválido, res = \"" + str(res) + "\"")

# FUNÇÕES PARA DEPURAÇÃO

def diagnosticos(val):
  global diags
  diags = val
  return

def verifica(obj, tipo, id, atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem): 

  ok = True # Este teste deu OK?

  if obj == None:
    sys.stderr.write("None\n")
  elif not type(obj) is tipo:
    aviso_prog("tipo do objeto " + str(type(obj)) + " inválido", True)
    ok = False
  else:
    sys.stderr.write("  testando {obtem_identificador()}:\n")
    id_cmp = obtem_identificador(obj)
    if id_cmp != id:
      aviso_prog("retornou " + str(id_cmp) + ", deveria ter retornado " + str(id), True)
      ok = False

    sys.stderr.write("  testando {obtem_atributos()}:\n")
    atrs_cmp = obtem_atributos(obj)
    if atrs_cmp != atrs:
      aviso_prog("retornou " + str(atrs_cmp) + ", deveria ter retornado " + str(atrs), True)
      ok = False
    
    sys.stderr.write("testando {busca_por_identificador()}:\n")
    obj1 = busca_por_identificador(id, cache, nome_tb, letra_tb, colunas, def_obj_mem)
    if obj1 != obj:
      aviso_prog("retornou " + str(obj1) + ", deveria ter retornado " + str(obj), True)
      ok = False

  return ok
