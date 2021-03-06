# Implementação do módulo {usuario} e da classe {Objeto_Usuario}.

import objeto
import usuario
import sessao
import compra
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

nome_tb = "usuarios"
  # Nome da tabela na base de dados.

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {Objeto_Usuario} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidadde dos objetos.

letra_tb = "U"
  # Prefixo dos identificadores de usuários

colunas = \
  (
    ( 'nome',          type("foo"), 'TEXT',    False ), # Nome completo.
    ( 'senha',         type("foo"), 'TEXT',    False ), # Senha de login.
    ( 'email',         type("foo"), 'TEXT',    False ), # Endereço de email
    ( 'CPF',           type("foo"), 'TEXT',    False ), # Número CPF ("{XXX}.{YYY}.{ZZZ}-{KK}")
    ( 'telefone',      type("foo"), 'TEXT',    False ), # Telefone com DDI e DDD ("+{XXX}({YYY}){MMMMM}-{NNNN}").
    ( 'documento',     type("foo"), 'TEXT',    True  ), # Número do documento de identidade (RG, pasaporte, etc.)
    ( 'milhagem',      type(10000), 'INTEGER', True  ),
    ( 'administrador', type(False), 'INTEGER', False ), # Define se o usuário é administrador (1=administrador)
  )
  # Descrição das colunas da tabela na base de dados.
  
diags = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

# Definição interna da classe {Objeto_Usuario}:

class Objeto_Usuario_IMP(objeto.Objeto):

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
  if diags: mostra(0,"usuario_IMP.cria(" + str(atrs) + ") ...")

  erros = valida_atributos(None, atrs_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  usr = objeto.cria(atrs_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert type(usr) is usuario.Objeto_Usuario
  return usr

def muda_atributos(usr, mods_mem):
  global cache, nome_tb, letra_tb, colunas, diags

  erros = valida_atributos(usr, mods_mem)
  if len(erros) != 0: raise ErroAtrib(erros)
  
  sys.stderr.write("\n")
  sys.stderr.write("usr antes = %s\n" % str(usr))
  sys.stderr.write("mods_mem = %s\n" % str(mods_mem))
  objeto.muda_atributos(usr, mods_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  sys.stderr.write("usr depois = %s\n" % str(usr))
  sys.stderr.write("\n")
  return

def obtem_identificador(usr):
  global cache, nome_tb, letra_tb, colunas, diags
  assert usr != None
  return objeto.obtem_identificador(usr)

def obtem_atributos(usr):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributos(usr)

def obtem_atributo(usr, chave):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributo(usr,chave)

def busca_por_identificador(id):
  global cache, nome_tb, letra_tb, colunas, diags
  usr = objeto.busca_por_identificador(id, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert usr == None or type(usr) is usuario.Objeto_Usuario
  return usr

def busca_por_email(em):
  global cache, nome_tb, letra_tb, colunas, diags
  unico = True
  id  = objeto.busca_por_campo('email', em, unico, cache, nome_tb, letra_tb, colunas)
  return id

def busca_por_CPF(CPF):
  global cache, nome_tb, letra_tb, colunas, diags
  unico = True
  id = objeto.busca_por_campo('CPF', CPF, unico, cache, nome_tb, letra_tb, colunas)

  return id

def sessoes_abertas(usr):  
  id_usr = usuario.obtem_identificador(usr)
  ids_sessoes_usr = sessao.busca_por_usuario(id_usr) # IDs das sessões deste usuário.
  sessoes_usr = map(lambda id: sessao.busca_por_identificador(id), ids_sessoes_usr) # Pega objetos.
  # Filtra apenas as Sessoes que estao abertas
  abertas_usr = list(filter(lambda ses: sessao.aberta(ses), sessoes_usr))
  return abertas_usr
  
def compras_abertas(usr):
  id_usr = usuario.obtem_identificador(usr)
  ids_compras_usr = compra.busca_por_cliente(id_usr) # IDs das compras deste usuário.
  compras_usr = map(lambda id: compra.busca_por_identificador(id), ids_compras_usr) # Pega objetos.
  # Filtra apenas as compras que não estao finalizadas:
  abertas_usr = list(filter(lambda cpr: compra.obtem_status(cpr) != 'fechado', compras_usr))
  return abertas_usr
  
def poltronas_abertas(usr):
  id_usr = usuario.obtem_identificador(usr)
  
  abertas_usr = [].copy()
  ids_compras = compra.busca_por_cliente(id_usr)
  for id_cpr in ids_compras:
    cpr = compra.busca_por_identificador(id_cpr)
    assert cpr != None # Paranóia.
    # Pega o id das poltronas de cada uma dessas compras
    ids_poltronas = compra.obtem_poltronas(cpr)
    for id_pol in ids_poltronas:
      # Para cada um desses ids pega o objeto da poltrona
      pol = poltrona.busca_por_identificador(id_pol)
      assert pol != None # Paranóia.
      assert poltrona.obtem_atributo(pol, 'id_compra') == id_cpr # Paranóia.
      # Verifica se o trecho não foi encerrado
      id_trc = poltrona.obtem_atributo(pol, 'id_trecho')
      trc = trecho.busca_por_identificador(id_trc)
      if not trecho.obtem_atributo(trc, 'encerrado'):
        abertas_usr.append(pol)
  return abertas_usr
  
def cria_testes(verb):
  global cache, nome_tb, letra_tb, colunas, diags
  inicializa(True)
  lista_atrs = \
    [ 
      { # U-00000001
        'nome': "José Primeiro", 
        'senha': "123456789", 
        'email': "primeiro@gmail.com", 
        'CPF': "123.456.789-00", 
        'telefone': "+55(19)9 9876-5432",
        'documento': "1.234.567-9 SSP-SP",
        'milhagem': 100,
        'administrador': False,
      },
      { # U-00000002
        'nome': "João Segundo", 
        'senha': "987654321", 
        'email': "segundo@ic.unicamp.br", 
        'CPF': "987.654.321-99", 
        'telefone': "+55(19)9 9898-1212",
        'documento': 'CD98765-43 PF',
        'milhagem': 200,
        'administrador' : False,
      },
      { # U-00000003
        'nome': "Juca Terceiro", 
        'senha': "333333333", 
        'email': "terceiro@gmail.com", 
        'CPF': "111.111.111-11",
        'telefone': "+55(19)9 9999-9999",
        'documento': None,
        'milhagem': None,
        'administrador' : True,
      },
      { # U-00000004
        'nome': "Jurandir Quarto", 
        'senha': "111111111", 
        'email': "quarto@ic.unicamp.br", 
        'CPF': "222.222.222-22", 
        'telefone': "+55(19)9 9898-1211",
        'documento': '1.234.567-8 SSP-SP',
        'milhagem': 400,
        'administrador' : False,
      },
      { # U-00000005
        'nome': "Josenildo Quinto", 
        'senha': "222222222", 
        'email': "quinto@ic.unicamp.br", 
        'CPF': "333.333.333-33", 
        'telefone': "+55(19)9 9898-1213",
        'documento': '1.234.567-7 SSP-SP',
        'milhagem': 500,
        'administrador' : False,
      },
      { # U-00000006
        'nome': "Julio Sexto", 
        'senha': "444444444", 
        'email': "sexto@ic.unicamp.br", 
        'CPF': "444.444.444-44", 
        'telefone': "+55(19)9 9898-1214",
        'documento': '1.234.567-6 SSP-SP',
        'milhagem': 600,
        'administrador' : False,
      },
      { # U-00000007
        'nome': "Jeferson Setimo", 
        'senha': "555555555", 
        'email': "setimo@ic.unicamp.br", 
        'CPF': "555.555.555-55", 
        'telefone': "+55(19)9 9898-1215",
        'documento': '1.234.567-5 SSP-SP',
        'milhagem': 700,
        'administrador' : False,
      },
      { # U-00000008
        'nome': "Joaquim Oitavo", 
        'senha': "666666666", 
        'email': "oitavo@ic.unicamp.br", 
        'CPF': "666.666.666-66", 
        'telefone': "+55(19)9 9898-1216",
        'documento': '1.234.567-4 SSP-SP',
        'milhagem': None,
        'administrador' : True,
      },
      { # U-00000009
        'nome': "Jonas Nono", 
        'senha': "777777777", 
        'email': "nono@ic.unicamp.br", 
        'CPF': "777.777.777-77", 
        'telefone': "+55(19)9 9898-1217",
        'documento': '1.234.567-3 SSP-SP',
        'milhagem': None,
        'administrador' : True,
      },

    ]
  for atrs in lista_atrs:
    usr = cria(atrs)
    assert usr != None and type(usr) is usuario.Objeto_Usuario
    id_usr = usuario.obtem_identificador(usr)
    nome = usuario.obtem_atributo(usr,'nome')
    if verb: sys.stderr.write("usuário %s = \"%s\" criado\n" % (id_usr, nome))
  return

def confere_e_elimina_conf_senha(args):

  senha = (args['senha'] if 'senha' in args else None)
  if senha != None and senha != '':
    # Senha está sendo alterada/definida.  Precisa confirmar senha:
    if 'conf_senha' not in args:
      raise ErroAtrib([ "campo 'Confirmar Senha' 'e obrigatório", ])
    else:
      if senha != args['conf_senha']:
        raise ErroAtrib([ "senhas não batem", ])
   
  # Remove o campo 'conf_senha', não mais necessários
  if 'conf_senha' in args: del args['conf_senha']
  return

def verifica(usr, id, atrs):
  return objeto.verifica(usr, usuario.Objeto_Usuario, id, atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def diagnosticos(val):
  global cache, nome_tb, letra_tb, colunas, diags
  diags = val
  return

# FUNÇÕES INTERNAS

def valida_atributos(usr, atrs_mem):
  """Faz validações específicas nos atributos {atrs_mem}. Devolve uma lista 
  de strings com descrições dos erros encontrados.
  
  Se {usr} é {None}, supõe que um novo usuário está sendo criado. Se {usr}
  não é {None}, supõe que {atrs_mem} sao alterações a aplicar nesse
  usuário.
  
  Em qualquer caso, não pode haver na base nenhum usuário
  com mesmo email ou CPF. """
  global cache, nome_tb, letra_tb, colunas, diags
  
  erros = [].copy()
  
  # Validade dos campos fornecidos:
  if 'nome' in atrs_mem:
    erros += valida_campo.nome_de_usuario('nome', atrs_mem['nome'], False)
  if 'email' in atrs_mem:
    erros += valida_campo.email('Email', atrs_mem['email'], False)
  if 'CPF' in atrs_mem:
    erros += valida_campo.CPF('CPF', atrs_mem['CPF'], False)
  if 'telefone' in atrs_mem:
    erros += valida_campo.telefone('Telefone', atrs_mem['telefone'], False)
  if 'documento' in atrs_mem:
    erros += valida_campo.documento('Documento', atrs_mem['documento'], True)
  if 'milhagem' in atrs_mem:
    erros += valida_campo.milhagem('Milhagem', atrs_mem['milhagem'], True)
  if 'administrador' in atrs_mem:
    erros += valida_campo.cidade_UF('Administrador', atrs_mem['administrador'], False)
     
  # Pega a senha, se tiver:
  if 'senha' in atrs_mem:
    senha = atrs_mem['senha']
    if senha == '': senha = None
  else:
    senha = None
  
  # Valida a senha:
  erros += valida_campo.senha('Senha', senha, (usr != None))

  # Acrescenta 'administrador' se não está presente, converte para booleano se está:
  if 'administrador' not in atrs_mem:
    atrs_mem['administrador'] = False
  elif type(atrs_mem['administrador']) is not bool:
    atrs_mem['administrador'] = True
      
  # Verifica completude:
  nargs = 0 # Número de campos em {atrs_mem} reconhecidos.
  for chave, tipo_mem, tipo_sql, nulo_ok in colunas:
    if chave in atrs_mem:
      nargs += 1
    elif usr == None:
      erros.append("campo '" + chave + "' é obrigatório")

  if nargs < len(atrs_mem):
    # Não deveria ocorrer:
    erro_prog("campos espúrios em {atrs_mem} = " + str(atrs_mem) + "")
    
  # Verifica unicidade de email e CPF:
  for chave in ('CPF', 'email'):
    # Exige atributo {chave} único:
    if chave in atrs_mem:
      val = atrs_mem[chave]
      if chave == 'CPF':
        id_bus = busca_por_CPF(val)
      elif chave == 'email':
        id_bus = busca_por_email(val)
      # sys.stderr.write("\n\n  valida_atributos: chave = '" + chave + "' val = '" + str(val) + "' id_bus = " + str(id_bus) + "\n\n")
      if (id_bus != None) and ((usr == None) or (id_bus != usr.id)):
        erros.append("usuário com '" + chave + "' = '" + val + "' já existe: " + id_bus)
  return erros

def def_obj_mem(obj, id, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {Objeto_Usuario} com
  identificador {id} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *NÃO* é inserido na base de dados.

  Se {obj} não é {None}, deve ser um objeto da classe {Objeto_Usuario}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}. A entrada correspondente na base de dados *NÃO* é alterada.

  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas, diags
  if diags: mostra(0,"usuario_IMP.def_obj_mem(" + str(obj) + ", " + id + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    obj = cria_obj_mem(id, atrs_SQL)
  else:
    assert obj.id == id
    modifica_obj_mem(obj, atrs_SQL)
  if diags: mostra(2,"obj = " + str(obj))
  return obj
    
def cria_obj_mem(id, atrs_SQL):
  """Cria um novo objeto da classe {Objeto_Usuario} com
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

  # Paranóia: verifica de novo a unicidade de CPF e email:
  for chave in ('CPF', 'email'):
    if chave not in atrs_mem:
      erro_prog("falta atributo '" + chave + "'")
    else:
      val = atrs_mem[chave]
      unico = True
      id_bus = objeto.busca_por_campo(chave, val, unico, cache, nome_tb, letra_tb, colunas)
      if id_bus != None:
        erro_prog("usuário com '" + chave + "' = '" + val + "' já existe: " + id + " " + id_bus)
    
  obj = usuario.Objeto_Usuario(id, atrs_mem)
  return obj
  
def modifica_obj_mem(obj, atrs_SQL):
  """O parâmetro {obj} deve ser um objeto da classe {Objeto_Usuario}; nesse
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

  # Paranóia: verifica de novo a unicidade de CPF e email:
  for chave in ('CPF', 'email'):
    if chave in mods_mem:
      val = mods_mem[chave]
      unico = True
      id_bus = objeto.busca_por_campo(chave, val, unico, cache, nome_tb, letra_tb, colunas)
      if id_bus != None and id_bus != obj.id:
        erro_prog("usuário com '" + chave + "' = '" + val + "' já existe: " + id + " " + id_bus)

  # Modifica os atributos:
  for chave, val in mods_mem.items():
    if not chave in obj.atrs:
      erro_prog("chave '" + chave + "' inválida")
    val_velho = obj.atrs[chave]
    if val != None and val_velho != None and (not type(val_velho) is type(val)):
      erro_prog("tipo do campo '" + chave + "' incorreto")
    obj.atrs[chave] = val
  return obj
