import objeto
import poltrona
import trecho

import tabela_generica
import tabelas
import conversao_sql
import identificador
import valida_campo; from valida_campo import ErroAtrib
from utils_testes import erro_prog, mostra
import sys

# VARIÁVEIS GLOBAIS DO MÓDULO

nome_tb = "poltronas"
  # Nome da tabela na base de dados.

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {Objeto_Poltrona} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidadde dos objetos.

letra_tb = "A"
  # Prefixo dos identificadores de usuários

colunas = \
  (
    ( 'id_trecho',   type("foo"), 'TEXT',    False ), # Identificador "T-{NNNNNNNN}" do trecho.
    ( 'id_compra',   type("foo"), 'TEXT',    True  ), # Identificador "C-{NNNNNNNN}" da compra, ou {None}.
    ( 'oferta',      type(False), 'INTEGER', False ), # Diz se a poltrona está em oferta.
    ( 'numero',      type("foo"), 'TEXT',    False ), # Número da poltrona no veículo.
    ( 'bagagens',    type(25),    'INTEGER', True  ), # Quantidade de bagagens na compra, ou {None}.
    ( 'preco' ,      type(3.14),  'FLOAT',   False ), # Preço da passagem nesta poltrona.
  )
  # Descrição das colunas da tabela na base de dados.

diags = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

# Definição interna da classe {Objeto_Poltrona}:

class Objeto_Poltrona_IMP(objeto.Objeto):

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
  if diags: mostra(0,"poltrona_IMP.cria(" + str(atrs_mem) + ") ...")

  erros = valida_atributos(None, atrs_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  pol = objeto.cria(atrs_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert type(pol) is poltrona.Objeto_Poltrona
  return pol

def muda_atributos(pol, mods_mem):
  global cache, nome_tb, letra_tb, colunas, diags

  erros = valida_atributos(pol, mods_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  objeto.muda_atributos(pol, mods_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return

def obtem_identificador(pol):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_identificador(pol)

def obtem_atributos(pol):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributos(pol)

def obtem_atributo(pol, chave):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributo(pol,chave)

def busca_por_identificador(id):
  global cache, nome_tb, letra_tb, colunas, diags
  pol = objeto.busca_por_identificador(id, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert type(pol) is poltrona.Objeto_Poltrona
  return pol

def busca_por_trecho(trc):
  global cache, nome_tb, letra_tb, colunas, diags
  id_trc = trecho.obtem_identificador(trc)
  unico = False
  ids_poltronas = objeto.busca_por_campo('id_trecho', id_trc, unico, cache, nome_tb, letra_tb, colunas)
  return ids_poltronas

def busca_por_numero(trc):
  global cache, nome_tb, letra_tb, colunas, diags
  id_trc = trecho.obtem_identificador(trc)
  unico = False
  ids_poltronas = objeto.busca_por_campo('numero', id_trc, unico, cache, nome_tb, letra_tb, colunas)
  return ids_poltronas

def busca_por_compra(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  id_cpr = trecho.obtem_identificador(cpr)
  unico = False
  ids_poltronas = objeto.busca_por_campo('id_compra', id_cpr, unico, cache, nome_tb, letra_tb, colunas)
  return ids_poltronas

def lista_livres(trc):
  global cache, nome_tb, letra_tb, colunas, diags
  id_trc = trecho.obtem_identificador(trc)
  args = { 'id_trecho': id_trc, 'id_compra': None }
  unico = False
  ids_poltronas = objeto.busca_por_campos(args, unico, cache, nome_tb, letra_tb, colunas)
  return ids_poltronas

def busca_ofertas():
  global cache, nome_tb, letra_tb, colunas, diags
  args = { 'id_compra': None, 'oferta': True }
  unico = False
  ids_poltronas = objeto.busca_por_campos(args, unico, cache, nome_tb, letra_tb, colunas)
  return ids_poltronas

def cria_conjunto(trc, txt):
  global cache, nome_tb, letra_tb, colunas, diags
  
  id_trc = trecho.obtem_identificador(trc)
  
  if trc == None: raise ErroAtrib(["trecho não pode ser nulo"])
  # Obtém a lista de números de poltronas e respectivos preços:
  nums_precos = analisa_esp_conjunto(txt);
  pols = [].copy()
  for num, prc in nums_precos:
    if diags: sys.stderr.write("criando poltrona \"%s\" ($ %.2f) no trecho \"%s\"\n" % (num, prc, id_trc))
    erros = [].copy()
    erros += valida_campo.numero_de_poltrona("número de poltrona", num, False)
    erros += valida_campo.preco("preço", prc, False)
    if len(erros) > 0: raise ErroAtrib(erros)
    # !!! COMPLETAR !!!
    # pol = ...
    # pols.append(pol)
  return pols

def cria_testes():
  global cache, nome_tb, letra_tb, colunas, diags
  inicializa(True)
  lista_atrs = \
    [ 
      { 'id_trecho':  "T-00000001",
        'numero':     "01A",
        'oferta':     True,
        'id_compra':  "C-00000001",
        'preco':      10.00,
        'bagagens':   0,
      },
      { 'id_trecho':  "T-00000001",
        'numero':     "02A",
        'oferta':     True,
        'id_compra':  None,
        'preco':      60.00,
        'bagagens':   None,
      },
      { 'id_trecho':  "T-00000001",
        'numero':     "02B",
        'oferta':     False,
        'id_compra':  "C-00000002",
        'preco':      11.00,
        'bagagens':   1,
      },
      { 'id_trecho':  "T-00000002",
        'numero':     "31",
        'oferta':     True,
        'id_compra':  None,
        'preco':      20.00,
        'bagagens':   None,
      },
      { 'id_trecho':  "T-00000002",
        'numero':     "32",
        'oferta':     False,
        'id_compra':  None,
        'preco':      30.00,
        'bagagens':   None,
      },
      { 'id_trecho':  "T-00000002",
        'numero':     "33",
        'oferta':     False,
        'id_compra':  "C-00000001",
        'preco':      12.00,
        'bagagens':   2,
      },
      { 'id_trecho':  "T-00000003",
        'numero':     "31",
        'oferta':     True,
        'id_compra':  None,
        'preco':      50.00,
        'bagagens':   None,
      },
      { 'id_trecho':  "T-00000003",
        'numero':     "33",
        'oferta':     False,
        'id_compra':  "C-00000003",
        'preco':      13.00,
        'bagagens':   3,
      },
    ]
  for atrs in lista_atrs:
    pol = cria(atrs)
    assert pol != None and type(pol) is poltrona.Objeto_Poltrona
    id_ass = poltrona.obtem_identificador(pol)
    id_trc = poltrona.obtem_atributo(pol, 'id_trecho')
    id_cpr = poltrona.obtem_atributo(pol, 'id_compra')
    if id_cpr == None: id_cpr = "LIVRE"
    sys.stderr.write("poltrona %s no trecho %s (compra %s) criado\n" % (id_ass, id_trc, id_cpr))
  return

def verifica(pol, id, atrs):
  return objeto.verifica(pol, poltrona.Objeto_Poltrona, id, atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def diagnosticos(val):
  global cache, nome_tb, letra_tb, colunas, diags
  diags = val
  return

# FUNÇÕES AUXILIARES:

def analisa_esp_conjunto(txt):
  global cache, nome_tb, letra_tb, colunas, diags
  # !!! IMPLEMENTAR - use {analisa_esp_grupo} !!!
  nums_precos = [ ("4F", 90.0), ("4G", 90.0), ("29Z", 120.0), ] # Temporário para testes.
  return nums_precos
 
# FUNÇÕES INTERNAS
 
def analisa_esp_grupo(txt):
  """Destrincha a cadeia {txt}, no formato descrito na função
  {cria_conjunto}, exceto que não deve conter nenhum ponto-e-vírgula (';').
  Deve terminar com dois-pontos (':') e o preço.  Retorna uma lista de
  pares, cada par com um número de poltrona e esse preço."""
  global cache, nome_tb, letra_tb, colunas, diags
  # !!! IMPLEMENTAR -- use {analisa_esp_lista} !!!
  assert False
  
def analisa_esp_lista(txt, prc):
  """Destrincha a cadeia {txt}, que deve ser uma lista de
  itens separados por vírgulas (',').  Cada item deve ser
  um número de poltrona ou dois números separados por hifen ('-').
  Retorna uma lista de pares, cada par com um número de poltrona
  e o preço dado {prc}."""
  global cache, nome_tb, letra_tb, colunas, diags
  # !!! IMPLEMENTAR -- use {analisa_esp_intervalo} !!!
  assert False
  
def analisa_esp_intervalo(txt, prc):
  """Destrincha a cadeia {txt}, que deve ser dois números separados por hifen ('-').
  Retorna uma lista de pares, cada par com um número de poltrona
  e o preço dado {prc}. """
  global cache, nome_tb, letra_tb, colunas, diags
  # !!! IMPLEMENTAR !!!
  assert False

def valida_atributos(pol, atrs_mem):
  """Faz validações específicas nos atributos {atrs_mem}. Devolve uma lista
  de strings com descrições dos erros encontrados.

  Se {pol} é {None}, supõe que uma novo poltrona está sendo criado. Se {pol}
  não é {None}, supõe que {atrs_mem} sao alterações a aplicar essa
  poltrona.

  Em qualquer caso, não pode haver, ao mesmo tempo, duas poltronas com o mesmo número e trecho. """

  global cache, nome_tb, letra_tb, colunas, diags

  sys.stderr.write("!! valida_atributos atrs_mem = " + str(atrs_mem) + "\n")
  
  erros = [].copy();

  # Validade dos campos fornecidos:
  if 'id_trecho' in atrs_mem:
    erros += valida_campo.id_trecho('id_trecho', atrs_mem['id_trecho'], False)
  if 'id_compra' in atrs_mem:
    erros += valida_campo.id_compra('id_compra', atrs_mem['id_compra'], True)
  if 'oferta' in atrs_mem:
    erros += valida_campo.booleano('Oferta', atrs_mem['oferta'], False)
  if 'numero' in atrs_mem:
    erros += valida_campo.numero_de_poltrona('Numero', atrs_mem['numero'], False)
  if 'bagagens' in atrs_mem:
    erros += valida_campo.num_de_bagagens('Bagagens', atrs_mem['bagagens'], True)
  if 'preco' in atrs_mem:
    erros += valida_campo.preco('Preco', atrs_mem['preco'], False)

  # Verifica completude:
  nargs = 0 # Número de campos em {atrs_mem} reconhecidos.
  for chave, tipo_mem, tipo_sql, nulo_ok in colunas:
    if chave in atrs_mem:
      nargs += 1
    elif pol == None and not nulo_ok:
      # Criando objeto, todas as colunas obrigatórias devem ser especificadas:
      erros.append("campo '" + chave + "' é obrigatório")

  if nargs < len(atrs_mem):
    # Não deveria ocorrer:
    erro_prog("campos espúrios em {atrs_mem} = " + str(atrs_mem) + "")

  # Verifica unicidade da poltrona. Se for nova poltrona ({pol=None}),
  # não deve haver nenhuma poltrona na base com mesmo número e trecho.  Se for
  # alteração ({pol != None}), deve haver apenas uma, e deve ter
  # o mesmo identificador de {pol}.
  # !!! COMPLETAR -- usar {objeto.busca_por_campos} !!!

  return erros

def def_obj_mem(obj, id, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {Objeto_Poltrona} com
  identificador {id} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *NÃO* é inserido na base de dados.

  Se {obj} não é {None}, deve ser um objeto da classe {Objeto_Poltrona}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}. A entrada correspondente na base de dados *NÃO* é alterada.

  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas, diags
  if diags: mostra(0,"poltrona_IMP.def_obj_mem(" + str(obj) + ", " + id + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    obj = cria_obj_mem(id, atrs_SQL)
  else:
    assert obj.id == id
    modifica_obj_mem(obj, atrs_SQL)
  if diags: mostra(2,"obj = " + str(obj))
  return obj

def cria_obj_mem(id, atrs_SQL):
  """Cria um novo objeto da classe {Objeto_Poltrona} com
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

  obj = poltrona.Objeto_Poltrona(id, atrs_mem)
  return obj

def modifica_obj_mem(obj, atrs_SQL):
  """O parâmetro {obj} deve ser um objeto da classe {Objeto_Poltrona}; nesse
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
