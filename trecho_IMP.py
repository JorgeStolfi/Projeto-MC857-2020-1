import objeto
import usuario
import trecho
import poltrona

import tabela_generica
import tabelas
import conversao_sql
import identificador
import valida_campo; from valida_campo import ErroAtrib
from utils_testes import erro_prog, mostra
import sys

# VARIÁVEIS GLOBAIS DO MÓDULO
 
cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {Objeto_Trecho} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidade dos objetos.

nome_tb = "trechos"
  # Nome da tabela na base de dados.
 
letra_tb = "T"
  # Prefixo comum dos identificadores de trecho.

colunas = None
  # Descrição das colunas da tabela na base de dados.
  
diags = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

# Definição interna da classe {Objeto_Trecho}:

class Objeto_Trecho_IMP(objeto.Objeto):

  def __init__(self, id, atrs, poltronas):
    global cache, nome_tb, letra_tb, colunas, diags
    objeto.Objeto.__init__(self, id, atrs)
    self.poltronas = poltronas.copy()

# Implementações:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas, diags
  # Descrição da tabela "trechos". 
  colunas = \
    ( ( "codigo",       type("foo"), 'TEXT',    False ),  # Código do trecho na empresa (p. ex. "AZ 4623").
      ( "origem",       type("foo"), 'TEXT',    False ),  # Sigla da estação/porto/aeroporto de orígem.
      ( "destino",      type("foo"), 'TEXT',    False ),  # Sigla da estação/porto/aeroporto de destino.
      ( "dia_partida",  type("foo"), 'TEXT',    False ),  # Data UTC de partida, "{YYYY}-{MM}-{DD}".
      ( "hora_partida", type("foo"), 'TEXT',    False ),  # Hora UTC de partida, "{hh}:{mm}".
      ( "dia_chegada",  type("foo"), 'TEXT',    False ),  # Data UTC de chegada, "{YYYY}-{MM}-{DD}".
      ( "hora_chegada", type("foo"), 'TEXT',    False ),  # Hora UTC de chegada, "{hh}:{mm}".
      ( "veiculo",      type("foo"), 'TEXT',    False ),  # Código do veículo (onibus/aeronave)".
    )
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)
 
def cria(atrs_mem):
  global cache, nome_tb, letra_tb, colunas, diags

  erros = valida_atributos(None, atrs_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  trc = objeto.cria(atrs_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert type(trc) is trecho.Objeto_Trecho
  return trc

def obtem_identificador(trc):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_identificador(trc)

def obtem_atributos(trc):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributos(trc)

def obtem_atributo(trc, chave):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributo(trc,chave)

def obtem_poltronas(trc):
  global cache, nome_tb, letra_tb, colunas, diags
  id_trc = obtem_identificador(trc)
  return poltrona.busca_por_trecho(id_trc)

def busca(args):
  global cache, nome_tb, letra_tb, colunas, diags
  unico = False
  ids = objeto.busca_por_campos(args, unico, cache, nome_tb, letra_tb, colunas)
  return ids

def busca_por_identificador(id):
  global cache, nome_tb, letra_tb, colunas, diags
  trc = objeto.busca_por_identificador(id, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert trc == None or type(trc) is trecho.Objeto_Trecho 
  return trc

def busca_por_origem(cod):
  global cache, nome_tb, letra_tb, colunas, diags
  unico = False
  ids = objeto.busca_por_campo('codigo', cod, unico, cache, nome_tb, letra_tb, colunas)
  return ids

def busca_por_codigo_e_data(cod, dia, hora):
  global cache, nome_tb, letra_tb, colunas, diags
  args = { 'codigo': cod, 'dia_partida': dia, 'hora_partida': hora }
  unico = True
  ids = objeto.busca_por_campos(args, unico, cache, nome_tb, letra_tb, colunas)
  if ids == None:
    return None
  elif type(ids) is tuple or type(ids) is list:
    if len(ids) == 0:
      return None
    else:
      assert len(ids) == 1  # Pela unicidade de {(codigo,dia,hora)}.
      return busca_por_identificador(ids[0])
  else:
    # Tipo de retorno inválido -- não deveria acontecer:
    assert False 

def busca_por_origem_e_destino(origem, destino):
  global cache, nome_tb, letra_tb, colunas, diags
  args = { 'origem': origem, 'destino': destino }
  unico = False
  ids = objeto.busca_por_campos(args, unico, cache, nome_tb, letra_tb, colunas)
  return ids

def busca_por_dias(dia_min, dia_max):
  global cache, nome_tb, letra_tb, colunas, diags
  # !!! MUDAR PARA INTERVALO !!!
  unico = False
  ids = objeto.busca_por_campo("dia_partida", dia_min, unico, cache, nome_tb, letra_tb, colunas)
  if dia_min != dia_max:
    ids += objeto.busca_por_campo("dia_chegada", dia_max, unico, cache, nome_tb, letra_tb, colunas)
  return ids

def muda_atributos(trc, mods_mem):
  global cache, nome_tb, letra_tb, colunas, diags

  erros = valida_atributos(trc, mods_mem)
  if len(erros) != 0: raise ErroAtrib(erros)
  
  objeto.muda_atributos(trc, mods_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return

def cria_testes():
  global cache, nome_tb, letra_tb, colunas, diags
  inicializa(True)
  # Atributos dos trechos:
  lista_trechos = \
    [ { # T-00000001
        'codigo':       "AZ 4024",
        'origem':       "VCP",
        'destino':      "SDU",
        'dia_partida':  "2020-05-08",
        'hora_partida': "12:45",
        'dia_chegada':  "2020-05-08",
        'hora_chegada': "13:40",
        'veiculo':      "AAA-0001"
      },
      { # T-00000002
        'codigo':       "AZ 4036",
        'origem':       "SDU",
        'destino':      "VCP",
        'dia_partida':  "2020-05-08",
        'hora_partida': "19:45",
        'dia_chegada':  "2020-05-08",
        'hora_chegada': "20:40",
        'veiculo':      "AAA-0002"
      },
      { # T-00000003
        'codigo':       "GO 2133",
        'origem':       "SDU",
        'destino':      "VCP",
        'dia_partida':  "2020-05-08",
        'hora_partida': "19:33",
        'dia_chegada':  "2020-05-08",
        'hora_chegada': "20:27",
        'veiculo':      "AAA-0003"
      },
      { # T-00000004
        'codigo':       "AZ 4044",
        'origem':       "SDU",
        'destino':      "POA",
        'dia_partida':  "2020-05-08",
        'hora_partida': "20:00",
        'dia_chegada':  "2020-05-09",
        'hora_chegada': "06:25",
        'veiculo':      "AAA-0004"
      },
      { # T-00000005
        'codigo':       "AZ 4092",
        'origem':       "POA",
        'destino':      "MAO",
        'dia_partida':  "2020-05-09",
        'hora_partida': "07:40",
        'dia_chegada':  "2020-05-09",
        'hora_chegada': "13:20",
        'veiculo':      "AAA-0005"
      },
      { # T-00000006
        'codigo':       "GO 2121",
        'origem':       "SDU",
        'destino':      "MAO",
        'dia_partida':  "2020-05-08",
        'hora_partida': "15:00",
        'dia_chegada':  "2020-05-08",
        'hora_chegada': "19:33",
        'veiculo':      "AAA-0006"
      },
    ]
  for atrs in lista_trechos:
    trc = cria(atrs)
    assert trc != None and type(trc) is trecho.Objeto_Trecho
    id_trc = trecho.obtem_identificador(trc)
    sys.stderr.write("trecho %s criado\n" % id_trc)
  return

def verifica(trc, id, atrs):
  return objeto.verifica(trc, trecho.Objeto_Trecho, id, atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def diagnosticos(val):
  global cache, nome_tb, letra_tb, colunas, diags
  diags = val
  return

# FUNÇÕES INTERNAS

def valida_atributos(trc, atrs_mem):
  """Faz validação nos atributos {atrs_mem}. Devolve uma lista 
  de strings com descrições dos erros encontrados.
  
  Se {trc} é {None}, supõe que um novo pedido de trechos está sendo criado.
  Se {trc} não é {None}, supõe que {atrs_mem} sao alterações a aplicar nesse
  pedido de trecho. """
  global cache, nome_tb, letra_tb, colunas, diags
  
  erros = [].copy()
  
  return erros

def def_obj_mem(obj, id, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {Objeto_Trecho} com
  identificador {id} e atributos {atrs_SQL}, tais como extraidos
  da tabela de trechos.  Extrai a lista de poltronas da tabela
  correspondente, se houver. O objeto *NÃO* é inserido na base de dados. 
  
  Se {obj} não é {None}, deve ser um objeto da classe {Objeto_Trecho}; nesse
  caso a função altera os atributos de {obj}, exceto a lista de poltronas,
  conforme especificado em {atrs_SQL}. A entrada correspondente na 
  base de dados *NÃO* é alterada.
  
  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória. Se os parâmetros forem inválidos ou incompletos,
  retorna uma ou mais mensagens de erro, na forma de uma lista de strings."""
  global cache, nome_tb, letra_tb, colunas, diags
  if diags: mostra(0, "trecho_IMP.def_obj_mem(" + str(obj) + ", " + id + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, False, tabelas.id_para_objeto)
    if diags: mostra(2, "criando objeto, atrs_mem = " + str(atrs_mem))
    obj = trecho.Objeto_Trecho(id, atrs_mem, [].copy())
  else:
    assert obj.id == id
    mods_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, True, tabelas.id_para_objeto)
    if diags: mostra(2, "modificando objeto, mods_mem = " + str(mods_mem))
    assert type(mods_mem) is dict
    if len(mods_mem) > len(obj.atrs):
      erro_prog("numero excessivo de atributos a alterar")
    for chave, val in mods_mem.items():
      if not chave in obj.atrs:
        erro_prog("chave '" + chave + "' inválida")
      val_velho = obj.atrs[chave]
      if not type(val_velho) is type(val):
        erro_prog("tipo do campo '" + chave + "' incorreto")
      if chave == 'cliente' and val != val_velho:
        erro_prog("campo '" + chave + "' não pode ser alterado")
      obj.atrs[chave] = val
  if diags: mostra(2, "obj = " + str(obj))
  return obj
 
