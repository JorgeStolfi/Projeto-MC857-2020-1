import objeto
import usuario
import compra
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
  # Dicionário que mapeia identificadores para os objetos {Objeto_Compra} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidade dos objetos.

nome_tb = "compras"
  # Nome da tabela na base de dados.

letra_tb = "C"
  # Prefixo comum dos identificadores de compra.

colunas = None
  # Descrição das colunas da tabela na base de dados.

diags = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

# Definição interna da classe {Objeto_Usuario}:

class Objeto_Compra_IMP(objeto.Objeto):

  def __init__(self, id, atrs, itens):
    global cache, nome_tb, letra_tb, colunas, diags
    objeto.Objeto.__init__(self, id, atrs)
    self.itens = itens.copy()

# Implementações:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas, diags
  # Descrição da tabela "compras".
  colunas = \
    ( ( "cliente",      usuario.Objeto_Usuario, 'TEXT',    False ),  # Objeto/id do usuário logado no pedido de compra.
      ( "status",       type("foo"),        'TEXT',    False ),  # Estado do pedido de compra ('aberto', etc.).
      ("nome_pass",     type("foo"),        'TEXT',    False), # Nome do passageiro da passagem comprada
    )
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)

def cria(cliente, nome_pass):
  global cache, nome_tb, letra_tb, colunas, diags

  atrs_mem = { 'cliente': cliente, 'status': 'aberto', 'nome_pass': nome_pass }

  erros = valida_atributos(None, atrs_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  cpr = objeto.cria(atrs_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert type(cpr) is compra.Objeto_Compra
  return cpr

def obtem_identificador(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_identificador(cpr)

def obtem_atributos(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributos(cpr)

def obtem_atributo(cpr, chave):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributo(cpr,chave)

def obtem_cliente(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributo(cpr, 'cliente')

def obtem_status(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributo(cpr, 'status')

def obtem_poltronas(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  ids_poltronas = poltrona.busca_por_compra(cpr)
  return ids_poltronas

def busca(args):
  global cache, nome_tb, letra_tb, colunas, diags
  unico = False
  ids = objeto.busca_por_campos(args, unico, cache, nome_tb, letra_tb, colunas)
  return ids

def busca_por_identificador(id):
  global cache, nome_tb, letra_tb, colunas, diags
  cpr = objeto.busca_por_identificador(id, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return cpr

def busca_por_cliente(id_cliente):
  unico = False
  ids_compras = objeto.busca_por_campo('cliente', id_cliente, unico, cache, nome_tb, letra_tb, colunas)
  return ids_compras

def calcula_preco(cpr):
  preco = 0
  for polt in obtem_poltronas(cpr):
    polt = poltrona.busca_por_identificador(polt)
    preco = preco + poltrona.obtem_atributo(polt,'preco')
  return preco

def muda_atributos(cpr, mods_mem):
  global cache, nome_tb, letra_tb, colunas, diags

  erros = valida_atributos(cpr, mods_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  objeto.muda_atributos(cpr, mods_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return

def fecha(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  if (cpr is not None) and (compra.obtem_atributo(cpr,'status')):
    mods_mem = { 'status': 'pagando' }
    muda_atributos(cpr, mods_mem)

def cria_testes():
  global cache, nome_tb, letra_tb, colunas, diags
  inicializa(True)
  # Identificador de usuários e lista de poltronas de cada pedido de compra:
  lista_ups = \
    [
      ("U-00000001", ("A-00000001", "A-00000003", ), "Amanda Castro"),
      ("U-00000001", ("A-00000004", "A-00000006", "A-00000002", ),"Gustavo Galvão"),
      ("U-00000002", ("A-00000005", ), "José Roberto")
    ]
  for id_cliente, ids_poltronas, nome_pass in lista_ups:
    cliente = usuario.busca_por_identificador(id_cliente)

    cpr = cria(cliente, nome_pass)
    assert cpr != None and type(cpr) is compra.Objeto_Compra
    id_cpr = compra.obtem_identificador(cpr)
    usr = compra.obtem_cliente(cpr)
    id_usr = usuario.obtem_identificador(usr) if usr != None else "ninguém"
    sys.stderr.write("compra %s de %s criada\n" % (id_cpr, id_usr))
  return

def verifica(cpr, id, atrs):
  return objeto.verifica(cpr, compra.Objeto_Compra, id, atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def diagnosticos(val):
  global cache, nome_tb, letra_tb, colunas, diags
  diags = val
  return

# FUNÇÕES INTERNAS

def valida_atributos(cpr, atrs_mem):
  """Faz validação nos atributos {atrs_mem}. Devolve uma lista
  de strings com descrições dos erros encontrados.

  Se {cpr} é {None}, supõe que um novo pedido de compras está sendo criado.
  Se {cpr} não é {None}, supõe que {atrs_mem} sao alterações a aplicar nesse
  pedido de compra. """
  global cache, nome_tb, letra_tb, colunas, diags

  erros = [].copy();

  return erros

def def_obj_mem(obj, id, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {Objeto_Compra} com
  identificador {id} e atributos {atrs_SQL}, tais como extraidos
  da tabela de compras.  Extrai a lista de itens da tabela
  correspondente, se houver. O objeto *NÃO* é inserido na base de dados.

  Se {obj} não é {None}, deve ser um objeto da classe {Objeto_Compra}; nesse
  caso a função altera os atributos de {obj}, exceto a lista de itens,
  conforme especificado em {atrs_SQL}. A entrada correspondente na
  base de dados *NÃO* é alterada.

  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória. Se os parâmetros forem inválidos ou incompletos,
  retorna uma ou mais mensagens de erro, na forma de uma lista de strings."""
  global cache, nome_tb, letra_tb, colunas, diags
  if diags: mostra(0, "compra_IMP.def_obj_mem(" + str(obj) + ", " + id + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, False, tabelas.id_para_objeto)
    if diags: mostra(2, "criando objeto, atrs_mem = " + str(atrs_mem))
    obj = compra.Objeto_Compra(id, atrs_mem, [].copy())
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
