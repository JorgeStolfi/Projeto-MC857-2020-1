import objeto
import usuario
import compra

import tabela_generica
import tabelas
import conversao_sql
import identificador
import valida_campo; from valida_campo import ErroAtrib
from utils_testes import erro_prog, mostra

# VARIÁVEIS GLOBAIS DO MÓDULO
 
cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {ObjCompra} na memória.
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

# Definição interna da classe {ObjUsuario}:

class ObjCompra_IMP(objeto.Objeto):

  def __init__(self, id, atrs, itens):
    global cache, nome_tb, letra_tb, colunas, diags
    objeto.Objeto.__init__(self, id, atrs)
    self.itens = itens.copy()

# Implementações:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas, diags
  # Descrição da tabela "compras". 
  colunas = \
    ( ( "cliente",      usuario.ObjUsuario, 'TEXT',    False ),  # Objeto/id do usuário logado no pedido de compra.
      ( "status",       type("foo"),        'TEXT',    False ),  # Estado do pedido de compra ('aberto', etc.).
    )
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)
 
def cria(cliente):
  global cache, nome_tb, letra_tb, colunas, diags
  
  atrs_mem = { 'cliente': cliente, 'status': 'aberto' }

  erros = valida_atributos(None, atrs_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  cpr = objeto.cria(atrs_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert type(cpr) is compra.ObjCompra
  return cpr

def obtem_identificador(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_identificador(cpr)

def obtem_atributos(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributos(cpr)

def obtem_cliente(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributos(cpr, 'cliente')

def obtem_status(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributos(cpr, 'status')

def obtem_itens(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return cpr.itens.copy()

def busca_por_identificador(id):
  global cache, nome_tb, letra_tb, colunas, diags
  cpr = objeto.busca_por_identificador(id, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return cpr

def busca_por_cliente(id_cliente):
  erro_prog("Função não implementada")
  return None

def muda_atributos(cpr, mods_mem):
  global cache, nome_tb, letra_tb, colunas, diags

  erros = valida_atributos(cpr, mods_mem)
  if len(erros) != 0: raise ErroAtrib(erros)
  
  objeto.muda_atributos(cpr, mods_mem, cache, nome_tb, letra_tb, colunas)
  return

def fecha(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  if (cpr is not None) and (compra.obtem_atributo(cpr,'status')):
    mods_mem = { 'status': 'pagando' }
    muda_atributos(cpr, mods_mem)

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
  """Se {obj} for {None}, cria um novo objeto da classe {ObjCompra} com
  identificador {id} e atributos {atrs_SQL}, tais como extraidos
  da tabela de compras.  Extrai a lista de itens da tabela
  correspondente, se houver. O objeto *NÃO* é inserido na base de dados. 
  
  Se {obj} não é {None}, deve ser um objeto da classe {ObjCompra}; nesse
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
    obj = compra.ObjCompra(id, atrs_mem, [].copy())
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

# DEPURAÇÂO

def cria_testes():
  global cache, nome_tb, letra_tb, colunas, diags
  inicializa(True)
  # Identificador de usuários e lista de passagens de cada pedido de compra:
  lista_ups = \
    [
      ("U-00000001", ("P-00000001", "P-00000003", "P-00000002")),
      ("U-00000001", ("P-00000002", "P-00000003")),
      ("U-00000002", ( ))
    ]
  for id_cliente, ids_passagens in lista_ups:
    cliente = usuario.busca_por_identificador(id_cliente)
    cpr = cria(cliente)
    assert cpr != None and type(cpr) is compra.ObjCompra
    # for id_pass in ids_passagens:
    #   pass = passagem.busca_por_identificador(id_pass)
    #   acrescenta_passagem(cpr, pass)
  return

def diagnosticos(val):
  global cache, nome_tb, letra_tb, colunas, diags
  diags = val
  return
