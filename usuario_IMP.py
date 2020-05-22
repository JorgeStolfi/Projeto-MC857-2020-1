# Implementação do módulo {usuario} e da classe {Objeto_Usuario}.

import objeto
import usuario

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

  objeto.muda_atributos(usr, mods_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return

def obtem_identificador(usr):
  global cache, nome_tb, letra_tb, colunas, diags
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
  assert type(usr) is usuario.Objeto_Usuario
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

def cria_testes():
  global cache, nome_tb, letra_tb, colunas, diags
  inicializa(True)
  lista_atrs = \
    [ 
      {
        'nome': "José Primeiro", 
        'senha': "123456789", 
        'email': "primeiro@gmail.com", 
        'CPF': "123.456.789-00", 
        'telefone': "+55(19)9 9876-5432",
        'documento': "1.234.567-9 SSP-SP",
        'administrador': False,
      },
      {
        'nome': "João Segundo", 
        'senha': "987654321", 
        'email': "segundo@ic.unicamp.br", 
        'CPF': "987.654.321-99", 
        'telefone': "+55(19)9 9898-1212",
        'documento': 'CD98765-43 PF',
        'administrador' : False,
      },
      {
        'nome': "Juca Terceiro", 
        'senha': "333333333", 
        'email': "terceiro@gmail.com", 
        'CPF': "111.111.111-11",
        'telefone': "+55(19)9 9999-9999",
        'documento': None,
        'administrador' : True,
      }
    ]
  for atrs in lista_atrs:
    usr = cria(atrs)
    assert usr != None and type(usr) is usuario.Objeto_Usuario
    id_usr = usuario.obtem_identificador(usr)
    nome = usuario.obtem_atributo(usr,'nome')
    sys.stderr.write("usuário %s = \"%s\" criado\n" % (id_usr, nome))
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
  
  erros = [].copy();
  
  # Validade dos campos fornecidos:
  if 'nome' in atrs_mem:
    erros += valida_campo.nome_de_usuario('nome', atrs_mem['nome'], False)
  if 'email' in atrs_mem:
    erros += valida_campo.email('Email', atrs_mem['email'], False)
  if 'CPF' in atrs_mem:
    erros += valida_campo.CPF('CPF', atrs_mem['CPF'], False)
  if 'telefone' in atrs_mem:
    erros += valida_campo.telefone('Telefone', atrs_mem['telefone'], False)
  if 'administrador' in atrs_mem:
    erros += valida_campo.cidade_UF('Administrador', atrs_mem['administrador'], False)
  if 'documento' in atrs_mem:
    erros += valida_campo.cidade_UF('Documento', atrs_mem['documento'], True)
     
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
