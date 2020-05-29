# Imlementação do módulo {valida_campo}

import sys, re
import valida_campo
from math import floor

def nome_de_usuario(rotulo, val, nulo_ok):
  erros = []
  if val == None:
    if not nulo_ok: erros += [ "campo '%s' não pode ser omitido" % rotulo, ]
  else:
    if type(val) is not str:
      erros += [ "campo '%s' = \"%s\" deve ser string" % (rotulo, str(val)) ]
    else:
      n = len(val)
      if n < 6:
        erros += [ "campo '%s' (%d caracteres) muito curto" % (rotulo,n), ]
      elif n > 60:
        erros += [ "nome de usuário (%d caracteres) muito longo" % (rotulo,n), ]
      # !!! Verificar caracteres permitidos !!!
  return erros

def CPF(rotulo, val, nulo_ok):
  erros = []
  if val == None:
    if not nulo_ok: erros += [ "campo '%s' não pode ser omitido" % rotulo, ]
  else:
    if type(val) is not str:
      erros += [ "campo '%s' = \"%s\" deve ser string" % (rotulo, str(val)) ]
    elif not re.match(r'^[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}$', val):
      erros += [ "campo '%s' tem formato inválido, deveria ser 'xxx.xxx.xxx-xx'" % rotulo ]
    # !!! Verificar dígitos de controle !!!
  return erros

def cidade_UF(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []
  
def senha(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []

def email(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []

# def endereco(rotulo, val, nulo_ok):
#   # !!! Implementar !!!
#   return []

def CEP(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []

def telefone(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []

def documento(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []

def booleano(rotulo, val, nulo_ok):
  erros = []
  if val == None:
    if not nulo_ok: erros += [ "campo '%s' não pode ser omitido" % rotulo, ]
  else:
    if not type(val) is bool:
      erros += [ "campo '%s' = \"%s\" deve ser booleano" % (rotulo, str(val)) ]
  return []
  
def identificador(rotulo, val, letra, nulo_ok):
  erros = []
  if val == None:
    if not nulo_ok: erros += [ "campo '%s' não pode ser omitido" % rotulo, ]
  else:
    if type(val) is not str:
      erros += [ "campo '%s' = \"%s\" deve ser string" % (rotulo, str(val)) ]
    else:
      n = len(val)
      if letra != None and n >= 1 and val[0] != letra:
        erros += [ "campo '%s' = \"%s\" deve comecar com %s" % (rotulo, val, letra) ]
      if n != 10 or not re.match(r'^[A-Z]-[0-9]*$', val):
        erros += [ "campo '%s' = \"%s\" tem formato inválido" % (rotulo, val) ]
  return erros

def id_trecho(rotulo, val, nulo_ok):
  return identificador(rotulo, val, "T", nulo_ok)

def id_compra(rotulo, val, nulo_ok):
  return identificador(rotulo, val, "C", nulo_ok)

def numero_de_poltrona(rotulo, val, nulo_ok):
  erros = []
  if val == None:
      if not nulo_ok: erros += [ "campo '%s' não pode ser omitido" % rotulo, ]
  else:
    if type(val) is not str or not re.match(r'^[0-9]+[A-Z]?$', val):
      erros += [ "campo '%s' = \"%s\" tem formato inválido" % (rotulo, str(val)) ] 
  return erros

def num_de_bagagens(rotulo, val, nulo_ok):
  erros = []
  if val == None:
    if not nulo_ok: erros += [ "campo '%s' não pode ser omitido" % rotulo, ]
  else:
    if type(val) is not int or val < 0:
      erros += [ "campo '%s' = \"%s\" deve ser inteiro não-negativo" % (rotulo, str(val)) ] 
  return erros

def preco(rotulo, val, nulo_ok):
  erros = []
  if val == None:
    if not nulo_ok: erros += [ "campo '%s' não pode ser omitido" % rotulo, ]
  else:
    if type(val) is not float or val < 0:
      erros += [ "campo '%s' = \"%s\" deve ser float não-negativo" % (rotulo, str(val)) ]
    elif abs(val - 0.01*(floor(val/0.01 + 0.5))) > 1.0e-8: 
      erros += [ "campo '%s' = \"%s\" deve ser número inteiro de centavos" % (rotulo, str(val)) ]
  return erros


