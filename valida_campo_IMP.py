# Imlementação do módulo {valida_campo}

import sys, re
import valida_campo

def nome_de_usuario(rotulo, val, nulo_ok):
  if val == None and not nulo_ok: return [ "campo '%s' não pode ser omitido" % rotulo, ]
  erros = []
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
  if val == None and not nulo_ok: return [ "campo '%s' não pode ser omitido" % rotulo, ]
  erros = []
  if type(val) is not str:
    erros += [ "campo '%s' = \"%s\" deve ser string" % (rotulo, str(val)) ]
  elif not re.match(r'^[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}$', val):
    erros += [ "campo '%s' tem formato inválido, deveria ser 'xxx.xxx.xxx-xx'" % rotulo ]
  # !!! Verificar dígitos de controle !!!
  return erros
  
# def linha_de_endereco(rotulo, val, nulo_ok):
#   if val == None and not nulo_ok: return [ "campo '%s' não pode ser omitido" % rotulo, ]
#   erros = []
#   if type(val) is not str:
#     erros += [ "campo '%s' deve ser string" % rotulo ]
#   else:
#     n = len(val)
#     if n < 2:
#       erros += [ "campo '%s' (%d caracteres) muito curto" % (rotulo,n), ]
#     elif n > 60:
#       erros += [ "nome de usuário (%d caracteres) muito longo" % (rotulo,n), ]
#     # !!! Verificar caracteres permitidos !!!
#   return erros

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

def administrador(rotulo, val, nulo_ok):
  # !!! Implementar !!!
  return []

def id_trecho(rotulo, val, nulo_ok):
  if val == None and not nulo_ok: return [ "campo '%s' não pode ser omitido" % rotulo, ]
  erros = []
  if type(val) is not str:
    erros += [ "campo '%s' = \"%s\" deve ser string" % (rotulo, str(val)) ]
  else:
    n = len(val)
    if n < 10:
      erros += [ "campo '%s' (%d caracteres) muito curto" % (rotulo,n), ]
    elif n > 10:
      erros += [ "campo '%s' (%d caracteres) muito longo" % (rotulo,n), ]
    elif n == 10:
      if val[:2] != str("T-"):
        erros += [ "campo '%s' = \"%s\" deve ser comecar com T-" % (rotulo, str(val)) ]
  return erros

def id_compra(rotulo, val, nulo_ok):
  if val == None and not nulo_ok: return [ "campo '%s' não pode ser omitido" % rotulo, ]
  erros = []
  if type(val) is not str:
    erros += [ "campo '%s' = \"%s\" deve ser string" % (rotulo, str(val)) ]
  else:
    n = len(val)
    if n < 10:
      erros += [ "campo '%s' (%d caracteres) muito curto" % (rotulo,n), ]
    elif n > 10:
      erros += [ "campo '%s' (%d caracteres) muito longo" % (rotulo,n), ]
    elif n == 10:
      if val[:2] != str("C-"):
        erros += [ "campo '%s' = \"%s\" deve ser comecar com C-" % (rotulo, str(val)) ]
  return erros

def oferta(rotulo, val, nulo_ok):
  if val == None and not nulo_ok: return [ "campo '%s' não pode ser omitido" % rotulo, ]
  erros = []
  if type(val) is not bool:
    erros += [ "campo '%s' = \"%s\" deve ser booleano" % (rotulo, str(val)) ]
  return erros

def numero(rotulo, val, nulo_ok):
  if val == None and not nulo_ok: return [ "campo '%s' não pode ser omitido" % rotulo, ]
  erros = []
  if type(val) is not str:
    erros += [ "campo '%s' = \"%s\" deve ser integer" % (rotulo, str(val)) ]
  return erros

def bagagens(rotulo, val, nulo_ok):
  if val == None and not nulo_ok: return [ "campo '%s' não pode ser omitido" % rotulo, ]
  erros = []
  if type(val) is not int:
    erros += [ "campo '%s' = \"%s\" deve ser integer" % (rotulo, str(val)) ]
  return erros

def preco(rotulo, val, nulo_ok):
  if val == None and not nulo_ok: return [ "campo '%s' não pode ser omitido" % rotulo, ]
  erros = []
  if type(val) is not str:
    erros += [ "campo '%s' = \"%s\" deve ser string" % (rotulo, str(val)) ]
  #else: 
    #if(val.find(".") == -1):
    #   erros += [ "campo '%s' = \"%s\" deve ter formatado os centavos no formato 00.00" % (rotulo, str(val)) ]
  return erros


