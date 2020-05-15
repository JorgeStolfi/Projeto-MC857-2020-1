# Implementação do módulo {assento} e da classe {Objeto_Assento}.

import objeto
import assento
import trecho

import tabela_generica
import tabelas
import conversao_sql
import identificador
import valida_campo; from valida_campo import ErroAtrib
from utils_testes import erro_prog, mostra
import sys

# VARIÁVEIS GLOBAIS DO MÓDULO

nome_tb = "assentos"
  # Nome da tabela na base de dados.

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {Objeto_Assento} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidadde dos objetos.

letra_tb = "A"
  # Prefixo dos identificadores de usuários

colunas = \
  (
    ( 'id_trecho',   type("foo"), 'TEXT',    False ), # Identificador "T-{NNNNNNNN}" do trecho
    ( 'id_compra',   type("foo"), 'TEXT',    True  ), # Identificador "C-{NNNNNNNN}" da compra, ou {None}.
    ( 'numero',      type("foo"), 'TEXT',    False ), # Número da poltrona no veículo
    ( 'preco' ,      type("foo"), 'TEXT',    False ), # 15-05 criaçao da coluna de preços
  )
  # Descrição das colunas da tabela na base de dados.
  
diags = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

# Definição interna da classe {Objeto_Assento}:

class Objeto_Assento_IMP(objeto.Objeto):

  def __init__(self, id, atrs):
    global cache, nome_tb, letra_tb, colunas
    objeto.Objeto.__init__(self, id, atrs)

# Implementação das funções:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas, diags
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)

def cria(atrs_mem):
  global cache, nome_tb, letra_tb, colunas, diags
  if diags: mostra(0,"assento_IMP.cria(" + str(atrs) + ") ...")

  erros = valida_atributos(None, atrs_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  ass = objeto.cria(atrs_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert type(ass) is assento.Objeto_Assento
  return ass

def muda_atributos(ass, mods_mem):
  global cache, nome_tb, letra_tb, colunas, diags

  erros = valida_atributos(ass, mods_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  objeto.muda_atributos(ass, mods_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return

def obtem_identificador(ass):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_identificador(ass)

def obtem_atributos(ass):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributos(ass)

def obtem_atributo(ass, chave):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributo(ass,chave)

def busca_por_identificador(id):
  global cache, nome_tb, letra_tb, colunas, diags
  ass = objeto.busca_por_identificador(id, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert type(ass) is assento.Objeto_Assento
  return ass

def busca_por_trecho(trc):
  global cache, nome_tb, letra_tb, colunas, diags
  id_trc = trecho.obtem_identificador(trc)
  return objeto.busca_por_campo('id_trecho', id_trc, cache, nome_tb, letra_tb, colunas)

def busca_por_compra(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  id_cpr = trecho.obtem_identificador(cpr)
  return objeto.busca_por_campo('id_compra', id_cpr, cache, nome_tb, letra_tb, colunas)

def cria_testes():
  global cache, nome_tb, letra_tb, colunas, diags
  inicializa(True)
  lista_atrs = \
    [ 
      { 'id_trecho': "T-00000001", 'numero': "01A", 'id_compra': "C-00000001", 'preco': "10" },
      { 'id_trecho': "T-00000001", 'numero': "02A", 'id_compra': None, 'preco': "0"  },
      { 'id_trecho': "T-00000001", 'numero': "02B", 'id_compra': "C-00000002", 'preco': "11" },
      { 'id_trecho': "T-00000002", 'numero': "31",  'id_compra': None, 'preco': "0"  },
      { 'id_trecho': "T-00000002", 'numero': "32",  'id_compra': None, 'preco': "0"  },
      { 'id_trecho': "T-00000002", 'numero': "33",  'id_compra': "C-00000001", 'preco': "12"},
      { 'id_trecho': "T-00000003", 'numero': "31",  'id_compra': None, 'preco': "0"  },
      { 'id_trecho': "T-00000003", 'numero': "33",  'id_compra': "C-00000003", 'preco': "13"},
    ]
  for atrs in lista_atrs:
    ass = cria(atrs)
    assert ass != None and type(ass) is assento.Objeto_Assento
    id_ass = assento.obtem_identificador(ass)
    id_trc = assento.obtem_atributo(ass, 'id_trecho')
    id_cpr = assento.obtem_atributo(ass, 'id_compra')
    if id_cpr == None: id_cpr = "LIVRE"
    sys.stderr.write("assento %s no trecho %s (compra %s) criado\n" % (id_ass, id_trc, id_cpr))
  return

def verifica(ass, id, atrs):
  return objeto.verifica(ass, assento.Objeto_Assento, id, atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def diagnosticos(val):
  global cache, nome_tb, letra_tb, colunas, diags
  diags = val
  return

# FUNÇÕES INTERNAS

def valida_atributos(ass, atrs_mem):
  """Faz validações específicas nos atributos {atrs_mem}. Devolve uma lista 
  de strings com descrições dos erros encontrados.
  
  Se {ass} é {None}, supõe que um novo usuário está sendo criado. Se {ass}
  não é {None}, supõe que {atrs_mem} sao alterações a aplicar nesse
  usuário.
  
  Em qualquer caso, não pode haver na base nenhum usuário
  com mesmo email ou CPF. """
  global cache, nome_tb, letra_tb, colunas, diags
  
  erros = [].copy();
  
  # Validade dos campos fornecidos:
  # !!! Completar !!!

  # Verifica completude:
  nargs = 0 # Número de campos em {atrs_mem} reconhecidos.
  for chave, tipo_mem, tipo_sql, nulo_ok in colunas:
    if chave in atrs_mem:
      nargs += 1
    elif ass == None:
      erros.append("campo '" + chave + "' é obrigatório")

  if nargs < len(atrs_mem):
    # Não deveria ocorrer:
    erro_prog("campos espúrios em {atrs_mem} = " + str(atrs_mem) + "")
    
  # Verifica unicidade de email e CPF:
  # !!! Completar !!!

  return erros

def def_obj_mem(obj, id, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {Objeto_Assento} com
  identificador {id} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *NÃO* é inserido na base de dados.

  Se {obj} não é {None}, deve ser um objeto da classe {Objeto_Assento}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}. A entrada correspondente na base de dados *NÃO* é alterada.

  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas, diags
  if diags: mostra(0,"assento_IMP.def_obj_mem(" + str(obj) + ", " + id + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    obj = cria_obj_mem(id, atrs_SQL)
  else:
    assert obj.id == id
    modifica_obj_mem(obj, atrs_SQL)
  if diags: mostra(2,"obj = " + str(obj))
  return obj
    
def cria_obj_mem(id, atrs_SQL):
  """Cria um novo objeto da classe {Objeto_Assento} com
  identificador {id} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *NÃO* é inserido na base de dados.
  
  Os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  
  global cache, nome_tb, letra_tb, colunas, diags

  # Converte atributos para formato na memória.  Todos devem estar presentes:
  atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, False, tabelas.id_para_objeto)
  if diags: mostra(2,"criando objeto, atrs_mem = " + str(atrs_mem))
  assert type(atrs_mem) is dict
  if len(atrs_mem) != len(colunas):
    erro_prog("numero de atributos = " + str(len(atrs_mem)) + " devia ser " + str(len(colunas)))

  obj = assento.Objeto_Assento(id, atrs_mem)
  return obj
  
def modifica_obj_mem(obj, atrs_SQL):
  """O parâmetro {obj} deve ser um objeto da classe {Objeto_Assento}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}.  A entrada correspondente da base de dados *NÃO* é alterada.

  Os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas, diags

  # Converte atributos para formato na memória. Pode ser subconjunto:
  mods_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, True, tabelas.id_para_objeto)
  if diags: mostra(2,"modificando objeto, mods_mem = " + str(mods_mem))
  assert type(mods_mem) is dict
  if len(mods_mem) > len(colunas):
    erro_prog("numero de atributos a alterar = " + str(len(mods_mem)) + " excessivo")

  # Modifica os atributos:
  for chave, val in mods_mem.items():
    if not chave in obj.atrs:
      erro_prog("chave '" + chave + "' inválida")
    val_velho = obj.atrs[chave]
    if val != None and val_velho != None and (not type(val_velho) is type(val)):
      erro_prog("tipo do campo '" + chave + "' incorreto")
    obj.atrs[chave] = val
  return obj
