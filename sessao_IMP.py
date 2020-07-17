import objeto
import sessao
import compra
import usuario

import tabela_generica
import tabelas
import conversao_sql
import identificador
import valida_campo; from valida_campo import ErroAtrib
from utils_testes import erro_prog, mostra
import sys

from datetime import datetime, timezone

# VARIÁVEIS GLOBAIS DO MÓDULO

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {Objeto_Sessao} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidade dos objetos.

nome_tb = "sessoes"
  # Nome da tabela na base de dados.

letra_tb = "S"
  # Prefixo comum dos identificadores de sessao.

colunas = None
  # Descrição das colunas da tabela na base de dados.

diags = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

# Definição interna da classe {Objeto_Usuario}:

class Objeto_Sessao_IMP(objeto.Objeto):

  def __init__(self, id_sessao, atrs):
    global cache, nome_tb, letra_tb, colunas, diags
    objeto.Objeto.__init__(self, id_sessao, atrs)


# Implementações:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas, diags
  colunas = \
    (
      ( "usr",          usuario.Objeto_Usuario, 'TEXT',    False ),  # Objeto/id do usuário logado na sessão.
      ( "criacao",      type("foo"),            'TEXT',    False ),  # Momento de criação da sessão.
      ( "abrt",         type(False),            'INTEGER', False ),  # Estado da sessao (1 = aberta).
      ( "cookie",       type("foo"),            'TEXT',    False ),  # Cookie da sessao.
      ( "carrinho",     compra.Objeto_Compra,   'TEXT',    True  ),  # Objeto compra que é o carrinho da sessão.
    )
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)

def cria(usr, cookie, carrinho):
  global cache, nome_tb, letra_tb, colunas, diags

  atrs_mem = {
    'usr': usr,
    'criacao': datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %z"),
    'abrt': True,
    'cookie': cookie,
    'carrinho' : carrinho
  }

  erros = valida_atributos(None, atrs_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  ses = objeto.cria(atrs_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert type(ses) is sessao.Objeto_Sessao
  return ses

def obtem_identificador(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  assert ses != None
  return objeto.obtem_identificador(ses)

def obtem_atributos(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributos(ses)

def obtem_atributo(ses, chave):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributo(ses, chave)

def obtem_usuario(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributo(ses,'usr')

def obtem_criacao(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributo(ses,'criacao')

def aberta(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributo(ses,'abrt')

def obtem_cookie(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributo(ses,'cookie')

def eh_administrador(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  if  ses == None or not aberta(ses): return False
  usr = obtem_usuario(ses)
  return usuario.obtem_atributo(usr, 'administrador')

def obtem_carrinho(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  return objeto.obtem_atributo(ses,'carrinho')

def busca_por_identificador(id):
  global cache, nome_tb, letra_tb, colunas, diags
  ses = objeto.busca_por_identificador(id, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return ses

def busca_por_usuario(id):
  global cache, nome_tb, letra_tb, colunas, diags
  ses = objeto.busca_por_campo("usr", id, False, cache, nome_tb, letra_tb, colunas)
  return ses

def busca_por_campo(chave, val):
    global cache, nome_tb, letra_tb, colunas, diags
    ids = objeto.busca_por_campo(chave, val, False, cache, nome_tb, letra_tb, colunas)
    return ids

def muda_atributos(ses, mods_mem):
  global cache, nome_tb, letra_tb, colunas, diags

  erros = valida_atributos(ses, mods_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  objeto.muda_atributos(ses, mods_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return

def fecha(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  if (ses is not None) and (sessao.obtem_atributo(ses,'abrt')):
    mods_mem = { 'abrt': False }
    muda_atributos(ses, mods_mem)

def cria_testes():
  global cache, nome_tb, letra_tb, colunas, diags
  inicializa(True)
  # Identificador de usuários e cookie de cada sessão:
  lista_ucs = \
    [
      ( "U-00000001", "ABCDEFGHIJK", "C-00000001" ), # S-00000001
      ( "U-00000001", "BCDEFGHIJKL", "C-00000002" ), # S-00000002
      ( "U-00000002", "CDEFGHIJKLM", "C-00000003" ), # S-00000003
      ( "U-00000003", "DEFGHIJKLMN", None         ), # S-00000004
    ]
  for id_usuario, cookie, id_carrinho in lista_ucs:
    usr = usuario.busca_por_identificador(id_usuario)
    assert usr != None and type(usr) is usuario.Objeto_Usuario
    if id_carrinho == None:
      carrinho = None
    else:
      carrinho = compra.busca_por_identificador(id_carrinho)
      assert carrinho != None and type(carrinho) is compra.Objeto_Compra
    ses = cria(usr, cookie, carrinho)
    assert ses != None and type(ses) is sessao.Objeto_Sessao
    id_ses = sessao.obtem_identificador(ses)
    usr = sessao.obtem_usuario(ses)
    id_usr = usuario.obtem_identificador(usr) if usr != None else "ninguém"
    sys.stderr.write("sessão %s de %s criada\n" % (id_ses, id_usr))
  return

def verifica(ses, id, atrs):
  return objeto.verifica(ses, sessao.Objeto_Sessao, id, atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def diagnosticos(val):
  global cache, nome_tb, letra_tb, colunas, diags
  diags = val
  return

# FUNÇÕES INTERNAS

def valida_atributos(ses, atrs_mem):
  """Faz validações específicas nos atributos {atrs_mem}. Devolve uma lista
  de strings com descrições dos erros encontrados.

  Se {ses} é {None}, supõe que um novo objeto de sessão está sendo criado.
  Se {ses} não é {None}, supõe que {atrs} sao alterações a aplicar nessa
  sessão. """
  global cache, nome_tb, letra_tb, colunas, diags
  erros = [].copy();
  return erros

def def_obj_mem(obj, id, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {Objeto_Sessao} com
  identificador {id} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *NÃO* é inserido na base de dados.

  Se {obj} não é {None}, deve ser um objeto da classe {Objeto_Sessao}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}. A entrada correspondente na base de dados *NÃO* é alterada.

  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas, diags
  if diags: mostra(0, "sessao_IMP.def_obj_mem(" + str(obj) + ", " + id + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, False, tabelas.id_para_objeto)
    if diags: mostra(2, "criando objeto, atrs_mem = " + str(atrs_mem))
    obj = sessao.Objeto_Sessao(id, atrs_mem)
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
      if chave == 'usr' and val != val_velho:
        erro_prog("campo '" + chave + "' não pode ser alterado")
      obj.atrs[chave] = val
  if diags: mostra(2, "obj = " + str(obj))
  return obj
