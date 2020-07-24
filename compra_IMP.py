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
import datetime

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
    ( ( "cliente",   usuario.Objeto_Usuario, 'TEXT',    False ), # Cliente que está montando o pedido de compra.
      ( "status",    type("foo"),            'TEXT',    False ), # Estado do pedido de compra ('aberto', etc.).
      ( "nome_pass", type("foo"),            'TEXT',    False ), # Nome do passageiro que vai fazer a viagem.
      ( "doc_pass",  type("foo"),             'TEXT',    True  ), # Número do documento de identidade (RG, pasaporte, etc.)
    )
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)

def cria(cliente, nome_pass, doc_pass):
  global cache, nome_tb, letra_tb, colunas, diags

  atrs_mem = { 'cliente': cliente, 'status': 'aberto', 'nome_pass': nome_pass, 'doc_pass': doc_pass}

  erros = valida_atributos(None, atrs_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  cpr = objeto.cria(atrs_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert type(cpr) is compra.Objeto_Compra
  return cpr

def obtem_identificador(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  assert cpr != None and type(cpr) is compra.Objeto_Compra
  return objeto.obtem_identificador(cpr)

def obtem_atributos(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  assert cpr != None and type(cpr) is compra.Objeto_Compra
  return objeto.obtem_atributos(cpr)

def obtem_atributo(cpr, chave):
  global cache, nome_tb, letra_tb, colunas, diags
  assert cpr != None and type(cpr) is compra.Objeto_Compra
  return objeto.obtem_atributo(cpr,chave)

def obtem_cliente(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  assert cpr != None and type(cpr) is compra.Objeto_Compra
  return objeto.obtem_atributo(cpr, 'cliente')

def obtem_status(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  assert cpr != None and type(cpr) is compra.Objeto_Compra
  return objeto.obtem_atributo(cpr, 'status')

def obtem_poltronas(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  assert cpr != None and type(cpr) is compra.Objeto_Compra
  ids_pols = poltrona.busca_por_compra(cpr)
  # ids_pols.sort(key = lambda id : poltrona.obtem_dia_e_hora_de_partida(poltrona.busca_por_identificador(id)))
  return ids_pols

def busca_por_campos(args):
  global cache, nome_tb, letra_tb, colunas, diags
  unico = False
  ids = objeto.busca_por_campos(args, unico, cache, nome_tb, letra_tb, colunas)
  return ids

def busca_por_identificador(id):
  global cache, nome_tb, letra_tb, colunas, diags
  if id == None: return None
  assert type(id) is str and (id[0] == letra_tb)
  cpr = objeto.busca_por_identificador(id, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return cpr

def busca_por_cliente(id_cliente):
  global cache, nome_tb, letra_tb, colunas, diags
  assert type(id_cliente) is str and (id_cliente[0] == "U")
  unico = False
  ids_compras = objeto.busca_por_campo('cliente', id_cliente, unico, cache, nome_tb, letra_tb, colunas)
  return ids_compras

def calcula_preco(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  assert cpr != None and type(cpr) is compra.Objeto_Compra
  preco = 0
  for polt in obtem_poltronas(cpr):
    polt = poltrona.busca_por_identificador(polt)
    preco = preco + poltrona.obtem_atributo(polt, 'preco')
  return preco

def muda_atributos(cpr, mods_mem):
  global cache, nome_tb, letra_tb, colunas, diags
  assert cpr != None and type(cpr) is compra.Objeto_Compra

  erros = valida_atributos(cpr, mods_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  objeto.muda_atributos(cpr, mods_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return

def verificar_baldeacao(cpr):

  # pega poltronas de compra, ordenadas por partida
  ids_poltronas = obtem_poltronas(cpr)
  obj_poltronas = []

  ultima_chegada = None
  ultimo_destino = None

  poltronas_invalidas = []
  for id_poltrona in ids_poltronas:

    # lendo poltrona atual
    obj_poltrona = poltrona.busca_por_identificador(id_poltrona)
    partida = poltrona.obtem_dia_e_hora_de_partida(obj_poltrona)
    chegada = poltrona.obtem_dia_e_hora_de_chegada(obj_poltrona)
    origem, destino = poltrona.obtem_origem_destino(obj_poltrona)

    # convertendo string para data
    formato = "%Y-%m-%d %H:%M UTC"
    partida = datetime.datetime.strptime(partida, formato)
    chegada = datetime.datetime.strptime(chegada, formato)

    # baldeacoes
    baldeacao_curta = datetime.timedelta(minutes=15)
    baldeacao_longa = datetime.timedelta(hours=2)

    # comparando com última poltrona
    if ultima_chegada is not None and ultimo_destino is not None:

        delta = partida - ultima_chegada
        # mudança de aeroporto, tempo de baldeação é de 2 horas
        if origem != ultimo_destino:
            if  delta < baldeacao_longa:
                poltronas_invalidas.append(id_poltrona)
        # mesmo aeroporto, tempo de baldeação é de 15 minutos
        else:
            if delta < baldeacao_curta:
                poltronas_invalidas.append(id_poltrona)

    ultima_chegada = chegada
    ultimo_destino = destino

  return poltronas_invalidas

def fecha(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  assert cpr != None and type(cpr) is compra.Objeto_Compra
  mods_mem = { 'status': 'pagando' }
  muda_atributos(cpr, mods_mem)

def cria_testes():
  global cache, nome_tb, letra_tb, colunas, diags
  inicializa(True)
  # Identificador de usuários e lista de poltronas de cada pedido de compra:
  lista_cupsf = \
    [
<<<<<<< HEAD
      ( "C-00000001", "U-00000001", "Amanda Almeida",  "45.246.235-2",   True, ),
      ( "C-00000002", "U-00000001", "Basílio Barros",  "234.764.987-23", True, ),
      ( "C-00000003", "U-00000002", "Carlos Costa",    "76.863.987-5",   True, ),   
      ( "C-00000004", "U-00000002", "Diego Dias",      "654.987.098-09", False,), 
      ( "C-00000005", "U-00000002", "Romario Silva",   "122.787.038-05", False,), 
      ( "C-00000006", "U-00000001", "Fabio Santos",    "555.957.058-05", True, ), 
      ( "C-00000007", "U-00000001", "Renato Augusto",  "111.227.338-03", False,), 
      ( "C-00000008", "U-00000001", "Carlos Tevez",    "666.967.698-06", True, ), 
      ( "C-00000009", "U-00000002", "André Santos",    "554.181.018-01", False,), 
      ( "C-00000010", "U-00000002", "Victor Cantillo", "444.955.085-08", True, ), 
=======
      ( "C-00000001", "U-00000001", "Amanda Almeida", "45.246.235-2",   True,  ),
      ( "C-00000002", "U-00000001", "Basílio Barros", "234.764.987-23", True,  ),
      ( "C-00000003", "U-00000002", "Carlos Costa",   "76.863.987-5",   True,  ),
      ( "C-00000004", "U-00000002", "Diego Dias",     "654.987.098-09", False, ),
>>>>>>> Adiciona verificar_baldeacao a compra
    ]
  for id_cpr_esp, id_cliente, nome_pass, doc_pass, aberto in lista_cupsf:
    cliente = usuario.busca_por_identificador(id_cliente)

    cpr = cria(cliente, nome_pass, doc_pass)
    assert cpr != None and type(cpr) is compra.Objeto_Compra
    id_cpr = compra.obtem_identificador(cpr)
    if not aberto: compra.fecha(cpr)

    # Paranóia:
    assert id_cpr == id_cpr_esp
    cliente_1 = compra.obtem_cliente(cpr)
    id_cliente_1 = usuario.obtem_identificador(cliente_1)
    assert id_cliente_1 == id_cliente

    sys.stderr.write("compra %s de %s criada\n" % (id_cpr, id_cliente))
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
