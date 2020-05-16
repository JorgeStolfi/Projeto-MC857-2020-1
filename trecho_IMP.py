import objeto
import usuario
import trecho
import assento

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

# Definição interna da classe {Objeto_Usuario}:

class Objeto_Trecho_IMP(objeto.Objeto):

  def __init__(self, id, atrs, assentos):
    global cache, nome_tb, letra_tb, colunas, diags
    objeto.Objeto.__init__(self, id, atrs)
    self.assentos = assentos.copy()

# Implementações:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas, diags
  # Descrição da tabela "trechos". 
  colunas = \
    ( ( "codigo",       type("foo"), 'TEXT',    False ),  # Código do trecho na empresa (p. ex. "AZ 4623").
      ( "origem",       type("foo"), 'TEXT',    False ),  # Sigla da estação/porto/aeroporto de orígem.
      ( "destino",      type("foo"), 'TEXT',    False ),  # Sigla da estação/porto/aeroporto de destino.
      ( "dt_partida",   type("foo"), 'TEXT',    False ),  # Data e hora UTC de partida "{YYYY}-{MM}-{DD} {hh}:{mm}".
      ( "dt_chegada",   type("foo"), 'TEXT',    False ),  # Data e hora UTC de chegada "{YYYY}-{MM}-{DD} {hh}:{mm}".
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

def obtem_assentos(trc):
  global cache, nome_tb, letra_tb, colunas, diags
  id_trc = obtem_identificador(trc)
  return assento.busca_por_trecho(id_trc)

def busca_por_identificador(id):
  global cache, nome_tb, letra_tb, colunas, diags
  trc = objeto.busca_por_identificador(id, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return trc

def busca_por_origem(cod):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.busca_por_campo("codigo", cod, cache, nome_tb, letra_tb, colunas)

def busca_por_codigo_e_data(cod,dt):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.busca_por_dois_campos("codigo", cod, 'dt_partida', dt, cache, nome_tb, letra_tb, colunas)

def busca_por_origem_e_destino(origem, destino):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.busca_por_dois_campos("origem", origem, 'destino', destino, cache, nome_tb, letra_tb, colunas)

def busca_por_dias(dt):
  global cache, nome_tb, letra_tb, colunas, diags
  chaves = ["dt_partida"]
  valores = [dt[:10]]
  return tabela_generica.busca_por_semelhanca(nome_tb, letra_tb, colunas, chaves, valores)

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
    [ {
        'codigo':      "AZ 4024",
        'origem':      "VCP",
        'destino':     "SDU",
        'dt_partida':  "2020-05-08 12:45",
        'dt_chegada':  "2020-05-08 13:40",
      },
      {
        'codigo':      "AZ 4036",
        'origem':      "SDU",
        'destino':     "VCP",
        'dt_partida':  "2020-05-08 19:45",
        'dt_chegada':  "2020-05-08 20:40",
      },
      {
        'codigo':      "GO 2333",
        'origem':      "SDU",
        'destino':     "VCP",
        'dt_partida':  "2020-05-08 19:33",
        'dt_chegada':  "2020-05-08 20:27",
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
  
  erros = [].copy();
  
  return erros

def def_obj_mem(obj, id, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {Objeto_Trecho} com
  identificador {id} e atributos {atrs_SQL}, tais como extraidos
  da tabela de trechos.  Extrai a lista de assentos da tabela
  correspondente, se houver. O objeto *NÃO* é inserido na base de dados. 
  
  Se {obj} não é {None}, deve ser um objeto da classe {Objeto_Trecho}; nesse
  caso a função altera os atributos de {obj}, exceto a lista de assentos,
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
 
